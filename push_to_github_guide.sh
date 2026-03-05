#!/bin/bash

echo "=========================================="
echo "🚀 推送代码到 GitHub"
echo "=========================================="
echo ""
echo "方法 1：使用 Personal Access Token（推荐）"
echo "----------------------------------------"
echo ""
echo "1. 访问：https://github.com/settings/tokens"
echo "2. 点击 'Generate new token (classic)'"
echo "3. 勾选 'repo' 权限"
echo "4. 点击 'Generate token'"
echo "5. 复制生成的 token（只显示一次！）"
echo ""
echo "6. 然后在下面输入您的信息："
echo ""

read -p "请输入您的 GitHub 用户名 [jenniferliu821]: " username
username=${username:-jenniferliu821}

read -sp "请输入您的 Personal Access Token: " token
echo ""

if [ -z "$token" ]; then
    echo ""
    echo "❌ Token 不能为空！"
    echo ""
    echo "如果您还没有 Token，请："
    echo "1. 访问：https://github.com/settings/tokens"
    echo "2. 创建新的 Personal Access Token"
    echo "3. 再次运行此脚本"
    echo ""
    exit 1
fi

echo ""
echo "正在推送到 GitHub..."
echo ""

# 使用 token 推送
git remote set-url origin "https://${username}:${token}@github.com/jenniferliu821/translation-web-app.git"
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ 成功推送到 GitHub！"
    echo "=========================================="
    echo ""
    echo "验证地址：https://github.com/jenniferliu821/translation-web-app"
    echo ""
    echo "🎯 下一步：在 Railway 部署"
    echo "1. 访问：https://railway.app"
    echo "2. 登录并创建新项目"
    echo "3. 选择 GitHub 仓库：translation-web-app"
    echo "4. 设置环境变量 GOOGLE_API_KEY"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "❌ 推送失败"
    echo "=========================================="
    echo ""
    echo "可能的原因："
    echo "1. Token 无效或过期"
    echo "2. Token 没有 'repo' 权限"
    echo "3. 网络连接问题"
    echo ""
    echo "请检查后重试"
    echo ""
fi

# 清理 URL 中的 token（安全考虑）
git remote set-url origin "https://github.com/jenniferliu821/translation-web-app.git"
