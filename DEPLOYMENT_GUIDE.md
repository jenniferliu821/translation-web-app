# 🚀 部署指南 - 让同事也能访问翻译应用

## 📋 部署概述

我们将把这个翻译应用部署到 Railway 平台，这样任何人都可以通过一个公开的网址访问，而不仅仅是 `http://127.0.0.1:8080`。

---

## 第一步：推送代码到 GitHub ✅

### 1.1 推送代码

在终端中运行以下命令：

```bash
cd ~/Desktop/cursor/多语言翻译
git push origin main
```

**如果提示需要用户名和密码：**
- 用户名：`jenniferliu821`
- 密码：使用 **Personal Access Token**（不是 GitHub 登录密码）

**如果您还没有 Personal Access Token：**
1. 访问：https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成并复制 token（这个 token 只会显示一次！）
5. 将 token 作为密码输入

### 1.2 验证推送成功

访问您的 GitHub 仓库确认代码已上传：
https://github.com/jenniferliu821/translation-web-app

---

## 第二步：在 Railway 上部署 🚂

### 2.1 创建 Railway 账号

1. 访问：https://railway.app
2. 点击 "Start a New Project" 或 "Login"
3. 使用 GitHub 账号登录（推荐）

### 2.2 创建新项目

1. 登录后，点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 授权 Railway 访问您的 GitHub
4. 选择 `jenniferliu821/translation-web-app` 仓库

### 2.3 配置环境变量

**重要：** 部署前必须设置 API Key！

1. 在 Railway 项目页面，点击您的服务
2. 点击 "Variables" 标签
3. 添加环境变量：
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: `AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s`

4. 点击 "Add" 保存

### 2.4 等待部署完成

- Railway 会自动检测到这是一个 Python 项目
- 它会读取 `requirements.txt` 并安装依赖
- 它会使用 `Procfile` 中定义的启动命令
- 部署通常需要 2-5 分钟

### 2.5 获取公开网址

1. 部署成功后，在项目页面找到 "Settings" 标签
2. 点击 "Generate Domain"
3. Railway 会生成一个类似这样的网址：
   ```
   https://translation-web-app-production.up.railway.app
   ```
4. 这就是您的公开网址！

---

## 第三步：测试部署 🧪

### 3.1 访问应用

在浏览器中打开 Railway 生成的网址，您应该能看到翻译界面。

### 3.2 测试翻译功能

1. 上传一个测试 CSV 文件（例如 `example_input.csv`）
2. 点击"开始翻译"
3. 等待翻译完成
4. 下载结果文件

### 3.3 分享给同事

将 Railway 生成的网址分享给您的同事，他们可以：
- 在任何地方访问（不需要在同一网络）
- 在任何设备上访问（电脑、手机、平板）
- 直接使用，无需安装任何软件

---

## 📊 对比：本地 vs 云端部署

| 特性 | 本地运行 | Railway 部署 |
|------|---------|-------------|
| **访问地址** | `http://127.0.0.1:8080` | `https://your-app.up.railway.app` |
| **谁能访问** | 只有您的电脑 | 任何人，任何地方 |
| **需要运行** | 必须手动运行 `python app.py` | 自动运行，24/7 在线 |
| **电脑关机** | 应用停止 | 应用继续运行 |
| **适用场景** | 个人测试 | 团队协作 |

---

## 🔧 高级配置（可选）

### 自定义域名

如果您有自己的域名，可以在 Railway 中绑定：
1. 进入项目的 Settings
2. 点击 "Custom Domain"
3. 输入您的域名（如 `translate.yourcompany.com`）
4. 按照提示配置 DNS 记录

### 查看日志

如果应用出现问题：
1. 在 Railway 项目页面
2. 点击 "Deployments" 标签
3. 查看部署日志和运行日志

### 更新应用

当您修改代码后：
1. 推送到 GitHub：
   ```bash
   git add .
   git commit -m "更新说明"
   git push origin main
   ```
2. Railway 会自动检测到更新并重新部署

---

## 💰 费用说明

- Railway 提供免费套餐，每月有 $5 的免费额度
- 对于小型应用（如这个翻译工具），免费额度通常足够
- 如果超出免费额度，可以升级到付费计划（从 $5/月起）

---

## ❓ 常见问题

### 1. 部署失败怎么办？

**检查以下几点：**
- 确认 `GOOGLE_API_KEY` 环境变量已正确设置
- 查看 Railway 的部署日志，找出错误信息
- 确认所有文件都已推送到 GitHub

### 2. 应用可以访问但无法翻译？

**可能原因：**
- API Key 未设置或无效
- API 配额已用完
- 网络问题

**解决方法：**
- 在 Railway 中检查环境变量
- 查看应用日志

### 3. 如何更新 API Key？

1. 在 Railway 项目页面
2. 点击 "Variables"
3. 找到 `GOOGLE_API_KEY`
4. 点击编辑，输入新的 API Key
5. 保存后应用会自动重启

### 4. 可以暂停应用以节省费用吗？

可以！在 Railway 项目页面：
1. 点击服务右上角的 "..." 菜单
2. 选择 "Pause"
3. 需要时再点击 "Resume"

---

## 📞 需要帮助？

如果遇到问题：
1. 查看 Railway 官方文档：https://docs.railway.app
2. 查看项目的 GitHub Issues
3. 联系技术支持

---

## ✅ 部署清单

- [ ] 代码已推送到 GitHub
- [ ] Railway 账号已创建
- [ ] 项目已在 Railway 上创建
- [ ] `GOOGLE_API_KEY` 环境变量已设置
- [ ] 部署成功，应用正在运行
- [ ] 获取到公开网址
- [ ] 测试应用功能正常
- [ ] 已将网址分享给同事

---

**祝您部署顺利！** 🎉
