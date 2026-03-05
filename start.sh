#!/bin/bash

# 多语言翻译 Web 应用启动脚本

echo "=========================================="
echo "🌍 启动多语言翻译 Web 应用"
echo "=========================================="
echo ""

# 进入脚本所在目录
cd "$(dirname "$0")"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "请先安装 Python 3"
    exit 1
fi

# 启动应用
echo "🚀 正在启动服务器..."
echo ""
python3 app.py
