# 多语言翻译 Web 应用 - 使用说明

## 📋 功能介绍

这是一个基于网页的多语言翻译工具，支持以下功能：
- 上传 CSV 格式的待翻译文件
- 自动翻译成 11 种语言
- 下载 Excel 格式的翻译结果

## 🌍 支持的语言

- 🇸🇦 Arabic (阿拉伯语)
- 🇩🇪 German (德语)
- 🇺🇸 English (英语)
- 🇪🇸 Spanish (西班牙语)
- 🇫🇷 French (法语)
- 🇮🇩 Indonesian (印尼语)
- 🇮🇹 Italian (意大利语)
- 🇯🇵 Japanese (日语)
- 🇧🇷 Portuguese (葡萄牙语)
- 🇹🇷 Turkish (土耳其语)
- 🇨🇳 Chinese (简体中文)

## 🚀 安装步骤

### 1. 安装 Python 依赖

在终端中进入项目文件夹，运行：

```bash
pip install -r requirements.txt
```

或者逐个安装：

```bash
pip install Flask
pip install google-generativeai
pip install openpyxl
```

### 2. 启动应用

运行以下命令启动服务器：

```bash
python app.py
```

启动成功后，你会看到：

```
==================================================
🌍 多语言翻译 Web 应用
==================================================

访问地址: http://127.0.0.1:5000
按 Ctrl+C 停止服务器
```

### 3. 使用网页界面

1. 在浏览器中打开 `http://127.0.0.1:5000`
2. 点击或拖拽上传你的 input.csv 文件
3. 点击"开始翻译"按钮
4. 等待翻译完成（翻译过程中会显示加载动画）
5. 点击"下载结果文件"按钮下载翻译后的 Excel 文件

## 📁 输入文件格式

CSV 文件应包含以下列：

| Key Name | Source Language | Original Text |
|----------|----------------|---------------|
| key1     | English        | Hello         |
| key2     | Chinese        | 你好           |

## 📊 输出文件格式

输出的 Excel 文件包含以下列：

| key_name | ar | de | en | es | fr | in | it | ja | pt-BR | tr | zh-CN |
|----------|----|----|----|----|----|----|----|----|-------|-------|--------|
| key1     | ... | ... | Hello | ... | ... | ... | ... | ... | ... | ... | ... |

## ⚙️ 配置

如需更改 API Key，请编辑 `app.py` 文件的第 20 行：

```python
API_KEY = "你的API密钥"
```

## 🛑 停止服务器

在终端中按 `Ctrl+C` 即可停止服务器。

## 💡 提示

- 每次翻译之间会有 2 秒延迟，以避免 API 限流
- 上传文件大小限制为 16MB
- 翻译完成后的文件会临时保存在系统临时目录中
- 建议使用 Chrome、Firefox 或 Safari 浏览器访问

## ❓ 常见问题

### 1. 如何查看我的本地 IP 地址？

如果你想在同一网络的其他设备上访问，可以：
- Windows: 运行 `ipconfig` 查看 IPv4 地址
- Mac/Linux: 运行 `ifconfig` 或 `ip addr` 查看 IP 地址
- 然后在其他设备的浏览器中访问 `http://你的IP地址:5000`

### 2. 翻译失败怎么办？

- 检查网络连接是否正常
- 确认 API Key 是否有效
- 查看控制台是否有错误信息

### 3. 如何使用自己的 input.csv 文件？

确保你的 CSV 文件包含这三列：
- `Key Name`: 标识符
- `Source Language`: 源语言（如 English, Chinese 等）
- `Original Text`: 需要翻译的文本

## 📝 项目结构

```
多语言翻译/
├── app.py                    # Flask 应用主文件
├── translator final.py       # 原始命令行版本
├── requirements.txt          # Python 依赖
├── templates/
│   └── index.html           # 网页界面
└── README.md                # 本说明文件
```
