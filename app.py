"""
多语言翻译 Web 应用
使用 Flask 提供网页界面
"""

from flask import Flask, render_template, request, send_file, jsonify
import csv
import os
import time
import json
import re
import google.generativeai as genai
from datetime import datetime
from openpyxl import Workbook
from werkzeug.utils import secure_filename
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为 16MB
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

# ============================================
# ⚙️ 配置区域 - API Key
# ============================================
# 从环境变量读取 API Key
API_KEY = os.environ.get('GOOGLE_API_KEY', '')

# 如果没有设置 API Key，应用仍然可以启动，但翻译功能会在使用时提示错误
if not API_KEY:
    print("⚠️ 警告：未设置 GOOGLE_API_KEY 环境变量！")
    print("   请在 Railway 的 Variables 中添加 GOOGLE_API_KEY")
    print("   应用将继续运行，但翻译功能将不可用。")
# ============================================

# 支持的语言（表头顺序）
LANGUAGES = ["ar", "de", "en", "es", "fr", "in", "it", "ja", "pt-BR", "tr", "zh-CN"]

# 语言代码对应的英文名称
LANGUAGE_NAMES = {
    "ar": "Arabic",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "in": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "pt-BR": "Brazilian Portuguese",
    "tr": "Turkish",
    "zh-CN": "Simplified Chinese"
}

# 源语言名称映射到代码
SOURCE_LANGUAGE_MAP = {
    "english": "en",
    "arabic": "ar",
    "german": "de",
    "spanish": "es",
    "french": "fr",
    "indonesian": "in",
    "italian": "it",
    "japanese": "ja",
    "brazilian portuguese": "pt-BR",
    "portuguese": "pt-BR",
    "turkish": "tr",
    "chinese": "zh-CN",
    "simplified chinese": "zh-CN"
}


def setup_gemini():
    """配置 Gemini API"""
    if not API_KEY:
        raise ValueError("API Key 未配置！请联系管理员设置 GOOGLE_API_KEY 环境变量。")
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-3-flash-preview')
    return model


def get_source_lang_code(source_language_text):
    """将源语言文本转换为语言代码"""
    return SOURCE_LANGUAGE_MAP.get(source_language_text.strip().lower(), "en")


def translate_text(model, text, source_lang_code, max_retries=3):
    """
    使用 Gemini 翻译文本到所有目标语言
    """
    # 需要翻译的目标语言（排除源语言）
    target_langs = [lang for lang in LANGUAGES if lang != source_lang_code]

    # 构建翻译提示
    target_list = "\n".join([f"- {code}: {LANGUAGE_NAMES[code]}" for code in target_langs])

    prompt = f"""You are a professional translator. Translate the following text from {LANGUAGE_NAMES.get(source_lang_code, 'English')} to these languages:

{target_list}

Source text: "{text}"

IMPORTANT RULES:
1. Return ONLY a valid JSON object
2. Use language codes as keys exactly as shown above (e.g., "pt-BR", "zh-CN")
3. No markdown, no code blocks, no explanations
4. Provide natural, accurate translations

Example format: {{"ar": "Arabic text", "de": "German text", "es": "Spanish text"}}

Translate now:"""

    for attempt in range(max_retries):
        try:
            print(f"🔄 尝试翻译 (第 {attempt + 1}/{max_retries} 次): {text[:50]}...")
            response = model.generate_content(prompt)

            # 检查响应是否有效
            if not response.candidates:
                print(f"⚠️  没有候选响应，重试...")
                time.sleep(2)
                continue

            candidate = response.candidates[0]

            # 检查是否有内容
            if not candidate.content or not candidate.content.parts:
                print(f"⚠️  候选项无内容，重试...")
                time.sleep(2)
                continue

            response_text = candidate.content.parts[0].text.strip()
            print(f"✅ 收到响应: {response_text[:100]}...")

            # 清理可能的 markdown 代码块
            if response_text.startswith('```'):
                response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
                response_text = re.sub(r'\s*```$', '', response_text)

            # 解析 JSON
            translations = json.loads(response_text)
            print(f"✅ JSON 解析成功，翻译了 {len(translations)} 种语言")

            # 添加源语言原文
            translations[source_lang_code] = text

            return translations

        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析错误: {e}")
            print(f"   响应内容: {response_text[:200] if 'response_text' in locals() else 'N/A'}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {source_lang_code: text}
        except Exception as e:
            print(f"❌ 翻译错误: {type(e).__name__}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {source_lang_code: text}

    print(f"⚠️  所有重试失败，仅返回源语言")
    return {source_lang_code: text}


def read_input_csv(file_path):
    """读取输入的 CSV 文件"""
    rows = []
    encodings = ['utf-8', 'utf-8-sig', 'gbk', 'gb2312', 'latin-1']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            return rows
        except UnicodeDecodeError:
            continue
        except Exception:
            continue

    return []


def write_output_xlsx(results, output_path):
    """将翻译结果写入 xlsx 文件"""
    # 表头顺序：key_name, ar, de, en, es, fr, in, it, ja, pt-BR, tr, zh-CN
    fieldnames = ['key_name'] + LANGUAGES

    wb = Workbook()
    ws = wb.active

    # 写表头
    ws.append(fieldnames)

    # 写数据
    for result in results:
        row = [result['key_name']]
        for lang in LANGUAGES:
            row.append(result['translations'].get(lang, ''))
        ws.append(row)

    wb.save(output_path)


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    """处理翻译请求"""
    # 检查是否有文件上传
    if 'file' not in request.files:
        return jsonify({'error': '没有上传文件'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({'error': '只支持 CSV 文件'}), 400

    try:
        # 保存上传的文件
        filename = secure_filename(file.filename)
        temp_input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(temp_input_path)

        # 读取 CSV
        input_data = read_input_csv(temp_input_path)

        if not input_data:
            os.remove(temp_input_path)
            return jsonify({'error': '文件为空或格式错误'}), 400

        # 配置 Gemini
        print(f"🔧 配置 Gemini API...")
        if API_KEY:
            print(f"   API Key 长度: {len(API_KEY)}")
            print(f"   API Key 前缀: {API_KEY[:20]}...")
        else:
            print(f"   ❌ API Key 为空！")

        try:
            model = setup_gemini()
            print(f"✅ Gemini 配置完成")
        except ValueError as e:
            os.remove(temp_input_path)
            return jsonify({'error': f'API 配置错误: {str(e)}'}), 500

        # 执行翻译
        results = []
        total = len(input_data)
        print(f"📋 开始处理 {total} 条翻译任务...")

        for i, row in enumerate(input_data, 1):
            # 获取数据
            key_name = row.get('Key Name', '')
            source_lang_text = row.get('Source Language', 'English')
            original_text = row.get('Original Text', '')

            if not original_text:
                print(f"⚠️  第 {i} 行: 原文为空，跳过")
                continue

            source_lang_code = get_source_lang_code(source_lang_text)
            print(f"\n📝 [{i}/{total}] Key: {key_name}, 源语言: {source_lang_text} ({source_lang_code})")

            # 调用翻译
            translations = translate_text(model, original_text, source_lang_code)
            print(f"   翻译结果: {list(translations.keys())}")

            results.append({
                'key_name': key_name,
                'translations': translations
            })

            # 避免 API 限流
            if i < total:
                time.sleep(2)

        # 生成输出文件
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"translations_{timestamp}.xlsx"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        write_output_xlsx(results, output_path)

        # 删除临时输入文件
        os.remove(temp_input_path)

        # 返回下载链接
        return jsonify({
            'success': True,
            'download_url': f'/download/{output_filename}',
            'filename': output_filename
        })

    except Exception as e:
        return jsonify({'error': f'翻译过程出错: {str(e)}'}), 500


@app.route('/download/<filename>')
def download(filename):
    """下载翻译结果"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return "文件不存在", 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


if __name__ == '__main__':
    print("=" * 50)
    print("🌍 多语言翻译 Web 应用")
    print("=" * 50)

    # 从环境变量读取端口（Railway 会提供 PORT 环境变量）
    port = int(os.environ.get('PORT', 8080))

    print(f"\n访问地址: http://127.0.0.1:{port}")
    print("按 Ctrl+C 停止服务器\n")
    app.run(debug=False, host='0.0.0.0', port=port)
