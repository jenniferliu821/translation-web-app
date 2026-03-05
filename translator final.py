"""
多语言翻译 Agent
支持11种语言之间的互译
"""

import csv
import os
import time
import json
import re
import google.generativeai as genai
from datetime import datetime
from openpyxl import Workbook

# ============================================
# ⚙️ 配置区域 - API Key 在这里修改
# ============================================
API_KEY = "AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s"  
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
            response = model.generate_content(prompt)
            
            # 检查响应是否有效
            if not response.candidates:
                print(f"  ⚠️ 第{attempt+1}次尝试: API 返回空响应")
                time.sleep(2)
                continue
            
            candidate = response.candidates[0]
            
            # 检查是否有内容
            if not candidate.content or not candidate.content.parts:
                print(f"  ⚠️ 第{attempt+1}次尝试: 响应内容为空")
                time.sleep(2)
                continue
            
            response_text = candidate.content.parts[0].text.strip()
            
            # 清理可能的 markdown 代码块
            if response_text.startswith('```'):
                response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
                response_text = re.sub(r'\s*```$', '', response_text)
            
            # 解析 JSON
            translations = json.loads(response_text)
            
            # 添加源语言原文
            translations[source_lang_code] = text
            
            print(f"  ✅ 翻译成功")
            return translations
            
        except json.JSONDecodeError as e:
            print(f"  ⚠️ 第{attempt+1}次尝试: JSON 解析错误")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {source_lang_code: text}
        except Exception as e:
            error_msg = str(e)
            if "response.text" in error_msg and "valid `Part`" in error_msg:
                print(f"  ⚠️ 第{attempt+1}次尝试: 模型返回空内容，正在重试...")
            else:
                print(f"  ⚠️ 第{attempt+1}次尝试: {e}")
            
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            
            print(f"  ❌ 翻译失败，保留原文")
            return {source_lang_code: text}
    
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
            print(f"✅ 成功读取文件 (编码: {encoding})")
            return rows
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"读取错误: {e}")
            continue
    
    print("❌ 无法读取文件，请检查文件编码")
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
    print(f"✅ 结果已保存到: {output_path}")


def main():
    """主函数"""
    print("=" * 50)
    print("🌍 多语言翻译 Agent")
    print("=" * 50)
    
    # 检查 API Key
    if API_KEY == "在这里粘贴你的API_Key":
        print("\n❌ 错误: 请先在代码中设置你的 API Key")
        print("打开 translator.py，找到第 15 行，替换 API_KEY 的值")
        return
    
    # 设置 Gemini
    print("\n正在配置 Gemini API...")
    try:
        model = setup_gemini()
        print("✅ Gemini API 配置成功")
    except Exception as e:
        print(f"❌ API 配置失败: {e}")
        return
    
    # 获取输入文件
    input_file = input("\n请输入 CSV 文件路径 (或直接回车使用 input.csv): ").strip()
    if not input_file:
        input_file = "input.csv"
    
    if not os.path.exists(input_file):
        print(f"\n❌ 找不到文件: {input_file}")
        return
    
    # 读取输入
    print(f"\n正在读取: {input_file}")
    input_data = read_input_csv(input_file)
    
    if not input_data:
        print("❌ 文件为空或格式错误")
        return
    
    print(f"📄 找到 {len(input_data)} 条待翻译内容")
    
    # 执行翻译
    results = []
    success_count = 0
    fail_count = 0
    
    for i, row in enumerate(input_data, 1):
        # 获取数据
        key_name = row.get('Key Name', '')
        source_lang_text = row.get('Source Language', 'English')
        original_text = row.get('Original Text', '')
        
        
        if not original_text:
            print(f"[{i}] ⚠️ 跳过空行")
            continue
        
        source_lang_code = get_source_lang_code(source_lang_text)
        
        print(f"\n[{i}/{len(input_data)}] 翻译中...")
        print(f"  Key: {key_name}")
        print(f"  源语言: {source_lang_text} ({source_lang_code})")
        print(f"  文本: {original_text[:50]}...")
        
        # 调用翻译
        translations = translate_text(model, original_text, source_lang_code)
        
        # 统计成功/失败
        if len(translations) > 1:
            success_count += 1
        else:
            fail_count += 1
        
        results.append({
            'key_name': key_name,
            'translations': translations
        })
        
        # 避免 API 限流
        if i < len(input_data):
            time.sleep(2)
    
    # 输出结果
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"translations_{timestamp}.xlsx"
    
    print(f"\n正在保存结果...")
    write_output_xlsx(results, output_file)
    

    print("\n" + "=" * 50)
    print("🎉 翻译完成！")
    print(f"📄 输出文件: {output_file}")
    print(f"✅ 成功: {success_count} 条")
    if fail_count > 0:
        print(f"❌ 失败: {fail_count} 条")
    print("=" * 50)


if __name__ == "__main__":
    main()
    