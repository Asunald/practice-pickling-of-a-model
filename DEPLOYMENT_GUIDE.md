# 🚀 部署指南 - 完整步骤

## ✅ 已完成
- [x] 模型训练完成
- [x] 配置文件已修改（Huggingface用户名：Asunald）
- [x] GitHub仓库已创建：Asunald/practice-pickling-of-a-model

## 📋 接下来的步骤

### 步骤1：初始化Git仓库并推送到GitHub

在你的项目目录下运行以下命令：

```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: ML project with CI/CD"

# 设置主分支名称
git branch -M main

# 添加远程仓库
git remote add origin https://github.com/Asunald/practice-pickling-of-a-model.git

# 推送到GitHub
git push -u origin main
```

### 步骤2：在GitHub中设置Huggingface Token

1. 打开你的GitHub仓库：https://github.com/Asunald/practice-pickling-of-a-model

2. 点击 **Settings**（设置）

3. 在左侧菜单找到 **Secrets and variables** → **Actions**

4. 点击 **New repository secret**

5. 填写信息：
   - Name（名称）：`HF_TOKEN`
   - Secret（值）：`你的Huggingface token`（从 https://huggingface.co/settings/tokens 获取）

6. 点击 **Add secret**

### 步骤3：触发GitHub Actions

推送代码后会自动触发，或者手动触发：

1. 进入仓库的 **Actions** 标签页
2. 选择 "训练模型并上传到Huggingface" 工作流
3. 点击 **Run workflow** → **Run workflow**

### 步骤4：查看结果

**GitHub Actions日志：**
- https://github.com/Asunald/practice-pickling-of-a-model/actions

**Huggingface模型：**
- https://huggingface.co/Asunald/practice-pickling-of-a-model

**GitHub Releases：**
- https://github.com/Asunald/practice-pickling-of-a-model/releases

## 🔍 故障排查

### 如果推送失败
```bash
# 检查远程仓库地址
git remote -v

# 如果需要重新设置
git remote remove origin
git remote add origin https://github.com/Asunald/practice-pickling-of-a-model.git
```

### 如果GitHub Actions失败
1. 检查 HF_TOKEN 是否正确设置
2. 查看Actions日志中的错误信息
3. 确认Huggingface token有写入权限

### 测试本地上传（可选）
```bash
# 在命令行设置token（替换为你的实际token）
set HF_TOKEN=你的_huggingface_token

# 运行上传脚本
python upload_to_hf.py
```

## ✨ 完成后你会看到

1. ✅ GitHub仓库包含所有代码
2. ✅ GitHub Actions自动运行成功
3. ✅ Huggingface上有你的模型
4. ✅ GitHub Releases中有模型文件

## 📝 注意事项

⚠️ **安全提醒**：
- 不要将 `HF_TOKEN` 直接写在代码中
- 只在GitHub Secrets中设置
- 如果token泄露，立即在Huggingface中撤销并重新生成

## 🎉 下一步

完成后，你可以：
1. 修改模型代码，推送后自动重新训练
2. 在Huggingface上分享你的模型
3. 查看不同版本的Release
