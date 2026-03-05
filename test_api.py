"""
测试 Gemini API 是否正常工作
用于诊断 Railway 部署问题
"""

import os
import google.generativeai as genai

print("=" * 50)
print("🔍 Gemini API 诊断工具")
print("=" * 50)

# 1. 检查 API Key
API_KEY = os.environ.get('GOOGLE_API_KEY', 'AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s')
print(f"\n1. API Key 检查:")
print(f"   - 长度: {len(API_KEY)}")
print(f"   - 前缀: {API_KEY[:20]}...")
print(f"   - 来源: {'环境变量' if os.environ.get('GOOGLE_API_KEY') else '代码默认值'}")

# 2. 配置 Gemini
print(f"\n2. 配置 Gemini API...")
try:
    genai.configure(api_key=API_KEY)
    print("   ✅ 配置成功")
except Exception as e:
    print(f"   ❌ 配置失败: {e}")
    exit(1)

# 3. 创建模型
print(f"\n3. 创建模型...")
try:
    model = genai.GenerativeModel('gemini-3-flash-preview')
    print("   ✅ 模型创建成功")
except Exception as e:
    print(f"   ❌ 模型创建失败: {e}")
    exit(1)

# 4. 测试简单调用
print(f"\n4. 测试 API 调用...")
test_prompt = "Translate 'Hello' to Chinese. Return only the translation."

try:
    response = model.generate_content(test_prompt)
    print("   ✅ API 调用成功")
    print(f"\n   响应内容:")
    if response.candidates:
        candidate = response.candidates[0]
        if candidate.content and candidate.content.parts:
            print(f"   {candidate.content.parts[0].text}")
        else:
            print("   ⚠️  候选项没有内容")
            print(f"   完整候选项: {candidate}")
    else:
        print("   ⚠️  没有候选项")
        print(f"   完整响应: {response}")

except Exception as e:
    print(f"   ❌ API 调用失败: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# 5. 测试翻译格式
print(f"\n5. 测试翻译 JSON 格式...")
translation_prompt = """Translate "Hello" to these languages:
- es: Spanish
- fr: French
- ja: Japanese

Return ONLY a JSON object like: {"es": "Hola", "fr": "Bonjour", "ja": "こんにちは"}"""

try:
    response = model.generate_content(translation_prompt)
    if response.candidates and response.candidates[0].content:
        result_text = response.candidates[0].content.parts[0].text.strip()
        print(f"   ✅ 翻译响应:")
        print(f"   {result_text}")

        # 尝试解析 JSON
        import json
        try:
            parsed = json.loads(result_text)
            print(f"   ✅ JSON 解析成功: {parsed}")
        except:
            print(f"   ⚠️  JSON 解析失败，可能需要清理格式")
    else:
        print(f"   ⚠️  翻译响应为空")

except Exception as e:
    print(f"   ❌ 翻译测试失败: {e}")

print("\n" + "=" * 50)
print("✅ 诊断完成")
print("=" * 50)
