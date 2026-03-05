# 多语言翻译 Web 应用 - Railway 部署指南

## 🚀 部署到 Railway 的步骤

### 第一步：准备 GitHub 仓库

1. **创建 GitHub 仓库**
   - 访问：https://github.com/new
   - 输入仓库名称：`translation-web-app`（或其他名字）
   - 选择 `Public` 或 `Private`
   - 点击 `Create repository`

2. **上传代码到 GitHub**

   在终端执行以下命令：

   ```bash
   cd /Users/jennifer/Desktop/Cursor/多语言翻译

   # 初始化 git 仓库
   git init

   # 添加所有文件
   git add .

   # 创建第一次提交
   git commit -m "Initial commit: 多语言翻译 Web 应用"

   # 连接到你的 GitHub 仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
   git remote add origin https://github.com/YOUR_USERNAME/translation-web-app.git

   # 推送到 GitHub
   git branch -M main
   git push -u origin main
   ```

---

### 第二步：部署到 Railway

1. **注册 Railway 账号**
   - 访问：https://railway.app
   - 点击 `Login with GitHub`（用你的 GitHub 账号登录）
   - 授权 Railway 访问你的 GitHub

2. **创建新项目**
   - 点击 `New Project`
   - 选择 `Deploy from GitHub repo`
   - 选择你刚创建的 `translation-web-app` 仓库
   - Railway 会自动检测到这是 Python 项目并开始部署

3. **配置环境变量**
   - 在 Railway 项目页面，点击你的服务
   - 点击 `Variables` 标签
   - 添加环境变量：
     - 变量名：`GOOGLE_API_KEY`
     - 变量值：`AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s`
   - 点击 `Add` 保存

4. **生成公开域名**
   - 在项目页面，点击 `Settings` 标签
   - 找到 `Domains` 部分
   - 点击 `Generate Domain`
   - Railway 会生成一个类似 `xxx.up.railway.app` 的域名

5. **等待部署完成**
   - 在 `Deployments` 标签查看部署状态
   - 等待状态变为 ✅ `Success`
   - 点击生成的域名访问你的应用！

---

### 第三步：测试和使用

1. **访问你的应用**
   - 使用 Railway 生成的域名，例如：`https://your-app.up.railway.app`
   - 你会看到翻译界面

2. **分享给同事**
   - 直接把域名发给同事
   - 他们可以在任何地方访问
   - 无需安装任何软件

---

## 📝 更新代码

以后如果要修改代码：

```bash
cd /Users/jennifer/Desktop/Cursor/多语言翻译

# 修改代码后...
git add .
git commit -m "更新说明"
git push

# Railway 会自动检测更新并重新部署！
```

---

## ⚙️ 重要提示

### 环境变量（必须配置）

在 Railway 的 Variables 中必须添加：
- `GOOGLE_API_KEY`: 你的 Google API Key

### 文件说明

- ✅ `Procfile` - 告诉 Railway 如何启动应用
- ✅ `runtime.txt` - 指定 Python 版本
- ✅ `requirements.txt` - Python 依赖包
- ✅ `.gitignore` - Git 忽略文件
- ✅ `.env.example` - 环境变量示例（不包含真实密钥）

---

## 💰 费用

Railway 免费额度：
- 每月 $5 免费额度
- 包含 500 小时运行时间
- 100GB 带宽
- 对于这个翻译应用来说，**完全够用**！

如果超出免费额度，需要绑定信用卡。

---

## 🆘 遇到问题？

### 部署失败
- 检查 Railway 的 `Build Logs` 查看错误信息
- 确保 requirements.txt 中的包都能正常安装

### 应用无法访问
- 检查 `Variables` 中是否添加了 `GOOGLE_API_KEY`
- 查看 `Deploy Logs` 确认应用是否成功启动

### 翻译失败
- 确认 Google API Key 是否有效
- 检查 API 配额是否用完

---

## ✅ 检查清单

部署前确认：
- [ ] GitHub 仓库已创建
- [ ] 代码已推送到 GitHub
- [ ] Railway 账号已注册
- [ ] 项目已连接到 GitHub 仓库
- [ ] 环境变量 `GOOGLE_API_KEY` 已添加
- [ ] 域名已生成
- [ ] 部署状态为 Success
- [ ] 可以通过域名访问应用

---

🎉 完成后，你的多语言翻译工具就可以在全球任何地方访问了！
