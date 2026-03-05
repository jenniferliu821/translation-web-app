#!/bin/bash

# 使用 Personal Access Token 推送到 GitHub
# 更简单的交互式版本

echo "=================================="
echo "🚀 推送代码到 GitHub"
echo "=================================="
echo ""
echo "📍 仓库地址: https://github.com/jenniferliu821/translation-web-app"
echo ""
echo "⚠️  需要 Personal Access Token"
echo ""
echo "📝 如何获取 Token："
echo "1. 访问: https://github.com/settings/tokens"
echo "2. 点击 'Generate new token' → 'Generate new token (classic)'"
echo "3. Note: 输入 'Translation App'"
echo "4. Expiration: 选择 '90 days' 或 'No expiration'"
echo "5. 勾选权限: 勾选 'repo'"
echo "6. 点击 'Generate token'"
echo "7. 复制生成的 token (ghp_xxxxx...)"
echo ""
echo "=================================="
echo ""
echo "请输入你的 Personal Access Token："
read -s TOKEN
echo ""
echo "正在推送..."
echo ""

cd "/Users/jennifer/Desktop/Cursor/多语言翻译"

# 使用 token 推送
git push https://jenniferliu821:${TOKEN}@github.com/jenniferliu821/translation-web-app.git main

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "🎉 推送成功！"
    echo "=================================="
    echo ""
    echo "📍 查看你的代码："
    echo "   https://github.com/jenniferliu821/translation-web-app"
    echo ""
    echo "🚀 下一步：部署到 Railway"
    echo "   访问: https://railway.app"
    echo "=================================="
else
    echo ""
    echo "❌ 推送失败"
    echo "请检查 Token 是否正确"
fi
