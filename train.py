"""
简单的机器学习模型训练脚本
训练一个线性回归模型来预测学生成绩
"""
import numpy as np
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def generate_data():
    """生成模拟的学生学习数据"""
    np.random.seed(42)
    
    # 学习小时数（每周1-25小时）
    study_hours = np.random.uniform(1, 25, 100).reshape(-1, 1)
    
    # 考试分数（基础分50 + 每小时2分 + 随机噪声）
    test_scores = 50 + 2 * study_hours + np.random.normal(0, 5, 100).reshape(-1, 1)
    
    return study_hours, test_scores

def train_model():
    """训练模型"""
    print("🚀 开始训练模型...")
    
    # 生成数据
    X, y = generate_data()
    
    # 分割训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 创建并训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 评估模型
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"✅ 模型训练完成！")
    print(f"📊 系数: {model.coef_[0][0]:.2f} (每小时学习的分数增长)")
    print(f"📊 截距: {model.intercept_[0]:.2f} (基础分数)")
    print(f"📊 均方误差 (MSE): {mse:.2f}")
    print(f"📊 R² 分数: {r2:.2f}")
    
    return model, mse, r2

def save_model(model):
    """保存模型到本地"""
    os.makedirs('model', exist_ok=True)
    
    with open('model/student_score_predictor.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("💾 模型已保存到 model/student_score_predictor.pkl")

def create_model_card(mse, r2):
    """创建模型卡片（README）"""
    readme_content = f"""---
language: en
tags:
- sklearn
- linear-regression
- student-performance
license: mit
---

# 学生成绩预测模型

这是一个简单的线性回归模型，用于根据学习时间预测学生考试成绩。

## 模型信息

- **模型类型**: 线性回归 (scikit-learn)
- **任务**: 回归预测
- **输入**: 每周学习小时数
- **输出**: 预测的考试分数

## 性能指标

- **均方误差 (MSE)**: {mse:.2f}
- **R² 分数**: {r2:.2f}

## 使用方法

```python
import pickle
import numpy as np

# 加载模型
with open('student_score_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

# 预测
study_hours = np.array([[15]])  # 每周学习15小时
predicted_score = model.predict(study_hours)
print(f"预测分数: {{predicted_score[0][0]:.1f}}")
```

## 训练数据

模型使用模拟数据训练：
- 样本数量: 100
- 特征: 每周学习小时数 (1-25小时)
- 目标: 考试分数 (基于公式: 50 + 2 * 学习小时 + 噪声)

## 自动化

此模型通过 GitHub Actions 自动训练并上传到 Hugging Face。
"""
    
    os.makedirs('model', exist_ok=True)
    with open('model/README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("📝 模型卡片已创建")

if __name__ == "__main__":
    # 训练模型
    model, mse, r2 = train_model()
    
    # 保存模型
    save_model(model)
    
    # 创建模型卡片
    create_model_card(mse, r2)
    
    print("\n✨ 所有任务完成！")
