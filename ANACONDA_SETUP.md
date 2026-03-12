# Anaconda虚拟环境设置指南

## 📦 创建和激活虚拟环境

### 1. 创建新的conda环境
```bash
conda create -n ml_project python=3.10 -y
```

### 2. 激活环境
```bash
conda activate ml_project
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

或者使用conda安装：
```bash
conda install numpy=1.24.3 scikit-learn=1.3.0 -y
pip install huggingface-hub==0.17.3
```

### 4. 验证安装
```bash
python -c "import numpy; import sklearn; import huggingface_hub; print('所有依赖安装成功！')"
```

## 🚀 运行项目

### 训练模型
```bash
python train.py
```

### 测试上传（需要先设置HF_TOKEN）
```bash
# Windows CMD
set HF_TOKEN=your_huggingface_token_here
python upload_to_hf.py

# Windows PowerShell
$env:HF_TOKEN="your_huggingface_token_here"
python upload_to_hf.py
```

## 🔄 常用命令

### 查看所有conda环境
```bash
conda env list
```

### 退出当前环境
```bash
conda deactivate
```

### 删除环境（如果需要重新创建）
```bash
conda deactivate
conda env remove -n ml_project
```

### 导出环境配置
```bash
conda env export > environment.yml
```

## 📝 完整工作流程

```bash
# 1. 创建并激活环境
conda create -n ml_project python=3.10 -y
conda activate ml_project

# 2. 安装依赖
pip install -r requirements.txt

# 3. 训练模型
python train.py

# 4. 查看生成的文件
dir model

# 5. 完成后退出环境
conda deactivate
```

## ⚠️ 注意事项

1. 每次打开新的终端窗口，都需要重新激活环境：
   ```bash
   conda activate ml_project
   ```

2. 如果遇到权限问题，可以尝试：
   ```bash
   conda init
   ```
   然后重启终端

3. 确保Anaconda已添加到系统PATH中

## 🎯 快速开始（复制粘贴）

```bash
conda create -n ml_project python=3.10 -y && conda activate ml_project && pip install -r requirements.txt && python train.py
```
