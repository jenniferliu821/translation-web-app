# 🔒 API Key 安全指南

## ❌ 发生了什么

您的 API Key **被 Google 检测到公开泄露**，可能已被自动禁用。

**泄露原因：**
1. API Key 硬编码在 `app.py` 中
2. 代码推送到 GitHub（公开仓库）
3. Google 爬虫扫描到并自动禁用

---

## ✅ 解决步骤（按顺序）

### 1. 创建新的 API Key

访问：https://aistudio.google.com/app/apikey

1. 点击 **"Create API Key"**
2. 选择项目（或创建新项目）
3. **暂时不设置限制**（测试成功后再设置）
4. 复制新的 Key（格式：`AIzaSy...`）
5. **不要分享这个 Key！**

---

### 2. 在 Railway 更新环境变量

1. 打开 Railway 项目
2. 点击 **Variables** 标签
3. 找到 `GOOGLE_API_KEY`
4. 点击编辑
5. 粘贴新的 API Key
6. 保存

**Railway 会自动重启**（不需要重新部署）

---

### 3. 删除旧的 API Key

回到 Google AI Studio：
1. 找到旧的 Key：`AIzaSyCp5TKySowNOh20kOZ4ge5N4S6QSjANa0s`
2. 点击删除
3. 确认

---

### 4. 测试新 Key

1. 等待 Railway 重启（30秒）
2. 访问您的翻译网站
3. 上传 CSV 文件测试
4. **应该能看到翻译结果了！** ✅

---

## 🔒 防止再次泄露

### ✅ 已修复的代码

我已经修改了 `app.py`：
- ❌ 移除了硬编码的 API Key
- ✅ 只从环境变量读取
- ✅ 如果没有环境变量会报错

**这样即使代码公开，也不会泄露 Key！**

---

### 推送安全更新

```bash
cd ~/Desktop/cursor/多语言翻译
git add app.py
git commit -m "移除硬编码的 API Key，增强安全性"
git push origin main
```

Railway 会自动重新部署。

---

## 🔐 最佳实践

### ✅ 正确做法：
- 使用环境变量存储敏感信息
- 在 Railway Variables 中设置
- 代码中只引用变量名

### ❌ 错误做法：
- 在代码中硬编码 API Key
- 将 Key 提交到 Git
- 在聊天/文档中分享真实的 Key

---

## 🎯 时间线

1. **现在**：创建新的 API Key（2 分钟）
2. **然后**：在 Railway 更新环境变量（1 分钟）
3. **等待**：Railway 自动重启（30 秒）
4. **测试**：上传文件，查看翻译结果（1 分钟）

**总共约 5 分钟！**

---

## 📋 检查清单

- [ ] 创建了新的 API Key
- [ ] 在 Railway Variables 中更新了 `GOOGLE_API_KEY`
- [ ] 删除了旧的 API Key
- [ ] 测试翻译功能正常
- [ ] 推送了安全更新的代码

---

创建新 Key 后告诉我，我会帮您完成剩下的步骤！
