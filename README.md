# 学生成绩预测 - ML项目示例

这是一个简单的机器学习项目，演示如何：
- 训练一个scikit-learn模型
- 使用GitHub Actions自动化训练流程
- 自动上传模型到Huggingface Hub

## 📋 项目结构

```

.
├── train.py                    # 模型训练脚本
├── upload_to_hf.py            # 上传到Huggingface的脚本
├── requirements.txt           # Python依赖
├── .github/
│   └── workflows/
│       └── train-and-upload.yml  # GitHub Actions配置
└── model/                     # 训练后的模型文件（自动生成）
    ├── student_score_predictor.pkl
    └── README.md
```

## 🚀 快速开始

### 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 训练模型：
```bash
python train.py
```

3. 模型将保存在 `model/` 目录下

### 设置GitHub Actions自动化

1. **Fork或创建此仓库**

2. **获取Huggingface Token**
   - 访问 https://huggingface.co/settings/tokens
   - 创建一个新的token（需要写入权限）

3. **在GitHub中设置Secret**
   - 进入你的仓库 → Settings → Secrets and variables → Actions
   - 点击 "New repository secret"
   - 名称: `HF_TOKEN`
   - 值: 粘贴你的Huggingface token

4. **修改配置**
   - 编辑 `upload_to_hf.py` 文件
   - 将 `YOUR_USERNAME` 改为你的Huggingface用户名

5. **触发工作流**
   - 推送代码到main分支，或
   - 在GitHub Actions页面手动触发

## 📊 模型说明

这是一个简单的线性回归模型，用于预测学生考试成绩：
- **输入**: 每周学习小时数
- **输出**: 预测的考试分数
- **算法**: 线性回归 (scikit-learn)

## 🔄 CI/CD流程

每次推送到main分支时：
1. GitHub Actions自动触发
2. 安装Python依赖
3. 训练模型
4. 自动上传到Huggingface Hub
5. 创建GitHub Release并附带模型文件

## 📦 GitHub Release

每次成功训练后，会自动创建一个新的Release：
- 标签格式：`v20260312-143025`（时间戳）
- 包含模型文件：`student_score_predictor.pkl` 和 `README.md`
- 可以在仓库的 "Releases" 页面查看所有历史版本

## 📝 参考资料

- [Huggingface Hub文档](https://huggingface.co/docs/hub/index)
- [GitHub Actions文档](https://docs.github.com/en/actions)
- [scikit-learn文档](https://scikit-learn.org/)

## 📄 许可证

MIT License
