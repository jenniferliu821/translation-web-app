#!/bin/bash

# 多语言翻译应用 - GitHub 推送脚本
# GitHub 用户名: jenniferliu821

echo "=================================="
echo "🚀 准备推送到 GitHub"
echo "=================================="
echo ""

# 确保在正确的目录
cd "/Users/jennifer/Desktop/Cursor/多语言翻译"

echo "📍 当前目录: $(pwd)"
echo ""

# 检查 Git 状态
echo "📦 检查 Git 状态..."
git status
echo ""

# 添加远程仓库
echo "🔗 添加 GitHub 远程仓库..."
git remote add origin https://github.com/jenniferliu821/translation-web-app.git

# 检查是否成功
if [ $? -eq 0 ]; then
    echo "✅ 远程仓库添加成功！"
else
    echo "⚠️  远程仓库可能已存在，尝试更新..."
    git remote set-url origin https://github.com/jenniferliu821/translation-web-app.git
fi

echo ""

# 确保在 main 分支
echo "🌿 切换到 main 分支..."
git branch -M main
echo ""

# 推送到 GitHub
echo "⬆️  推送代码到 GitHub..."
echo "=================================="
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo "🎉 成功推送到 GitHub！"
    echo "=================================="
    echo ""
    echo "📍 你的仓库地址："
    echo "   https://github.com/jenniferliu821/translation-web-app"
    echo ""
    echo "🚀 下一步：部署到 Railway"
    echo "=================================="
    echo "1. 访问：https://railway.app"
    echo "2. 点击 'Login with GitHub' 登录"
    echo "3. 点击 'New Project'"
    echo "4. 选择 'Deploy from GitHub repo'"
    echo "5. 选择 'jenniferliu821/translation-web-app'"
    echo "6. 等待自动部署"
    echo "7. 添加环境变量："
    echo "   GOOGLE_API_KEY = AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s"
    echo "8. 生成域名：Settings → Domains → Generate Domain"
    echo "=================================="
else
    echo ""
    echo "❌ 推送失败！"
    echo ""
    echo "可能的原因："
    echo "1. GitHub 仓库还未创建"
    echo "   请访问：https://github.com/new"
    echo "   仓库名：translation-web-app"
    echo ""
    echo "2. 需要 GitHub 身份验证"
    echo "   如果提示输入密码，请使用 Personal Access Token"
    echo "   创建 Token：https://github.com/settings/tokens"
    echo ""
    echo "3. 仓库已存在但有冲突"
    echo "   尝试：git pull origin main --allow-unrelated-histories"
    echo ""
fi
