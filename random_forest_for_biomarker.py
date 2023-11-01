import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 准备数据
# 假设X是特征矩阵，y是对应的标签（0或1）
X = np.array(...)  # 替换为您的特征矩阵
y = np.array(...)  # 替换为您的标签

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 随机森林模型训练
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 特征重要性评估
feature_importances = rf.feature_importances_

# 生物标记物选择
threshold = 0.05  # 生物标记物的重要性阈值，根据需求调整
biomarkers = np.where(feature_importances > threshold)[0]

# 输出生物标记物
print("Selected biomarkers:")
for biomarker in biomarkers:
    print(f"Feature {biomarker}: Importance {feature_importances[biomarker]}")