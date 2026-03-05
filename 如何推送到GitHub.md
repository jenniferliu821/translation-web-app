# 如何推送到 GitHub（3 种方法）

## 方法 1：使用自动脚本（最简单）⭐

### 步骤：

1. **打开终端**，运行：
   ```bash
   cd ~/Desktop/cursor/多语言翻译
   ./push_to_github_guide.sh
   ```

2. **按照提示操作**：
   - 输入用户名（默认：jenniferliu821）
   - 输入 Personal Access Token

3. **等待推送完成**

---

## 方法 2：手动创建 Token 并推送

### 步骤 A：创建 Personal Access Token

1. 访问：https://github.com/settings/tokens
2. 点击 **"Generate new token (classic)"**
3. 设置：
   - Note（备注）：`Translation App`
   - Expiration（过期时间）：选择一个时间（建议：90 days）
   - 勾选权限：
     - ✅ **repo**（完整的仓库控制权限）
4. 滚动到底部，点击 **"Generate token"**
5. **立即复制 Token**（只显示一次！格式：`ghp_xxxxxxxxxxxx`）

### 步骤 B：使用 Token 推送

打开终端，运行：

```bash
cd ~/Desktop/cursor/多语言翻译

# 方式 1：直接在 URL 中使用 token（一次性）
git push https://jenniferliu821:你的token@github.com/jenniferliu821/translation-web-app.git main
```

**或者**

```bash
# 方式 2：使用 git push 命令，然后输入凭据
git push origin main
# 提示输入 Username：jenniferliu821
# 提示输入 Password：粘贴你的 token
```

---

## 方法 3：使用 GitHub Desktop（最友好）

如果您觉得命令行太复杂，可以使用 GitHub Desktop：

1. **下载并安装**：https://desktop.github.com
2. **登录 GitHub 账号**
3. **添加仓库**：
   - File → Add Local Repository
   - 选择：`~/Desktop/cursor/多语言翻译`
4. **推送**：
   - 点击右上角的 "Push origin"

---

## 验证推送成功

推送成功后，访问：
https://github.com/jenniferliu821/translation-web-app

您应该能看到：
- ✅ DEPLOYMENT_GUIDE.md
- ✅ 快速部署步骤.md
- ✅ 部署流程图.txt
- ✅ push_to_github_guide.sh

---

## 常见错误及解决

### ❌ "Authentication failed"
**原因**：Token 无效或过期
**解决**：重新创建 Token

### ❌ "Permission denied"
**原因**：Token 没有 `repo` 权限
**解决**：创建新 Token 时勾选 `repo`

### ❌ "could not read Username"
**原因**：无法自动获取凭据
**解决**：使用方法 1 或方法 3

---

## 推送成功后的下一步

✅ 代码已在 GitHub 上

🎯 **现在去 Railway 部署：**

1. 访问：https://railway.app
2. 使用 GitHub 登录
3. 创建新项目 → 选择 `translation-web-app` 仓库
4. 设置环境变量：`GOOGLE_API_KEY`
5. 生成公开域名
6. 测试并分享给同事！

详细步骤见：`快速部署步骤.md`
