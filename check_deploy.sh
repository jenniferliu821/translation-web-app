#!/bin/bash

# 多语言翻译应用 - 部署检查脚本

echo "🔍 检查 Railway 部署准备情况..."
echo ""

# 检查必需文件
echo "📋 检查必需文件..."
files=("Procfile" "runtime.txt" "requirements.txt" "app.py" "templates/index.html")
all_files_exist=true

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file 缺失！"
        all_files_exist=false
    fi
done

echo ""

# 检查 Git 状态
echo "📦 检查 Git 状态..."
if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "✅ Git 仓库已初始化"

    # 检查是否有提交
    if git log -1 > /dev/null 2>&1; then
        echo "✅ 已有提交记录"
        echo "   最后提交: $(git log -1 --pretty=format:'%s')"
    else
        echo "⚠️  还没有提交记录"
    fi

    # 检查远程仓库
    if git remote -v | grep -q origin; then
        echo "✅ 已配置远程仓库"
        echo "   $(git remote get-url origin)"
    else
        echo "⚠️  还没有配置远程 GitHub 仓库"
    fi
else
    echo "❌ Git 仓库未初始化"
    all_files_exist=false
fi

echo ""
echo "================================"

if [ "$all_files_exist" = true ]; then
    echo "✅ 所有检查通过！"
    echo ""
    echo "🚀 下一步操作："
    echo ""
    echo "1. 在 GitHub 创建新仓库："
    echo "   https://github.com/new"
    echo ""
    echo "2. 连接到 GitHub（替换 YOUR_USERNAME）："
    echo "   git remote add origin https://github.com/YOUR_USERNAME/translation-web-app.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    echo "3. 部署到 Railway："
    echo "   https://railway.app"
    echo "   - 用 GitHub 登录"
    echo "   - New Project → Deploy from GitHub repo"
    echo "   - 选择你的仓库"
    echo "   - 添加环境变量: GOOGLE_API_KEY"
    echo "   - Generate Domain"
    echo ""
    echo "📖 详细步骤请查看 DEPLOY.md"
else
    echo "❌ 检查失败，请修复以上问题"
fi

echo "================================"
