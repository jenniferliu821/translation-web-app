# 多语言翻译 Web 应用

一个简单易用的在线多语言翻译工具，支持上传 CSV 文件并自动翻译成 11 种语言。

## 🌍 支持的语言

- 阿拉伯语 (Arabic)
- 德语 (German)
- 英语 (English)
- 西班牙语 (Spanish)
- 法语 (French)
- 印尼语 (Indonesian)
- 意大利语 (Italian)
- 日语 (Japanese)
- 葡萄牙语 (Portuguese)
- 土耳其语 (Turkish)
- 简体中文 (Simplified Chinese)

## ✨ 功能特点

- 📤 支持 CSV 文件上传（拖拽或点击上传）
- 🤖 使用 Google Gemini AI 进行智能翻译
- 📊 自动生成 Excel 格式的翻译结果
- 🎨 美观的渐变色用户界面
- ⚡ 实时翻译进度显示
- 📥 一键下载翻译结果

## 🚀 快速开始

### 本地运行

1. 安装依赖：
```bash
pip3 install -r requirements.txt
```

2. 设置环境变量：
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

3. 运行应用：
```bash
python3 app.py
```

4. 访问：http://127.0.0.1:8080

### 部署到云端

详细部署指南请查看 [DEPLOY.md](DEPLOY.md)

推荐使用 Railway 进行部署，简单快速！

## 📋 CSV 文件格式

输入的 CSV 文件需要包含以下三列：

| Key Name | Source Language | Original Text |
|----------|----------------|---------------|
| welcome_message | English | Welcome to our app |
| goodbye_message | English | Thank you for visiting |

## 📥 输出格式

翻译完成后会生成一个 Excel 文件，包含：
- 第一列：Key Name（原始标识符）
- 第二列：Source Language（源语言）
- 第三列：Original Text（原始文本）
- 后续列：各语言的翻译结果

## 🔧 技术栈

- **后端框架**: Flask
- **AI 翻译**: Google Generative AI (Gemini)
- **文件处理**: OpenPyXL
- **前端**: HTML + CSS + JavaScript

## 📦 项目结构

```
多语言翻译/
├── app.py                  # Flask 主应用
├── templates/
│   └── index.html         # 网页界面
├── requirements.txt       # Python 依赖
├── Procfile              # Railway 部署配置
├── runtime.txt           # Python 版本
├── .gitignore           # Git 忽略文件
├── .env.example         # 环境变量示例
├── README.md            # 项目说明
├── DEPLOY.md            # 部署指南
└── example_input.csv    # 示例文件
```

## 🔐 环境变量

需要配置以下环境变量：

- `GOOGLE_API_KEY`: Google Generative AI 的 API 密钥
- `PORT`: 服务器端口（可选，默认 8080）

## 📝 许可证

MIT License

## 🙋 问题反馈

如有问题或建议，欢迎提出 Issue。

---

🎉 享受便捷的多语言翻译体验！
