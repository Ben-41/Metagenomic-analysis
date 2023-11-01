import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform, pdist
from skbio.stats.ordination import pcoa
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/FC_data_group/FC_IBS_HC_normed_4Aug2023.csv', index_col=0)




# 提取样本名称和物种名称
samples = data.iloc[:, 1:].columns.tolist()
species = data.iloc[:, 0].tolist()

# 提取相对丰度数据
abundance_data = data.iloc[:, 1:].values

# 读取Responder和Non-responder信息
responder_samples = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/responder_samples.csv')['sample'].tolist()
non_responder_samples = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/non_responder_samples.csv')['sample'].tolist()

# 剔除不属于Responder或Non-responder的样本

selected_samples = responder_samples + non_responder_samples
selected_indices = [samples.index(sample) for sample in selected_samples]
print(selected_indices)
abundance_data_selected = abundance_data[selected_indices]

# 计算距离矩阵
distance_matrix = squareform(pdist(abundance_data_selected, metric='euclidean'))

# 进行PCoA分析
result = pcoa(distance_matrix)

# 提取坐标
coordinates = result.samples.values

# 绘制Responder样本
responder_coordinates = coordinates[:len(responder_samples)]
plt.scatter(responder_coordinates[:, 0], responder_coordinates[:, 1], label='Responder')

# 绘制Non-responder样本
non_responder_coordinates = coordinates[len(responder_samples):]
plt.scatter(non_responder_coordinates[:, 0], non_responder_coordinates[:, 1], label='Non-responder')

# 添加标签
# for i, sample in enumerate(selected_samples):
#     plt.annotate(sample, (coordinates[i, 0], coordinates[i, 1]))

# 显示图例
plt.legend()

# 显示图形
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCoA Plot')
plt.show()