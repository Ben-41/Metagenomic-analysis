import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from adjustText import adjust_text
import pandas as pd
import numpy as np
# 假设有两个列表，存储了基因的折叠变化（fold change）和p-value值

def read_csv_file(filename,col):
    df = pd.read_csv(filename)
    Column_data = df.iloc[:,col]
    return Column_data

pathway_names = read_csv_file("/Users/ben/Documents/CDD/IBS/humann3_out/火山图-FC-FDR.csv",0)
fold_change = read_csv_file("/Users/ben/Documents/CDD/IBS/humann3_out/火山图-FC-FDR.csv",1)
p_values = read_csv_file("/Users/ben/Documents/CDD/IBS/humann3_out/火山图-FC-FDR.csv",2)

# 创建一个数据框
data = {'Fold Change': fold_change, 'p-value': p_values}
df = pd.DataFrame(data)

# 设置阈值
fold_change_threshold = 1
p_value_threshold = 0.05

# 根据阈值筛选显著差异的基因
significantly_upregulated = df[(df['Fold Change'] > fold_change_threshold) & (df['p-value'] < p_value_threshold)]
significantly_downregulated = df[(df['Fold Change'] < -fold_change_threshold) & (df['p-value'] < p_value_threshold)]

# 绘制火山图
matplotlib.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(10, 6))
plt.scatter(df['Fold Change'], -np.log10(df['p-value']), color='silver', alpha=1, edgecolors='black', linewidths=1)
plt.scatter(significantly_upregulated['Fold Change'], -np.log10(significantly_upregulated['p-value']), color='red', label='Upregulated', edgecolors='black', linewidths=1)
plt.scatter(significantly_downregulated['Fold Change'], -np.log10(significantly_downregulated['p-value']), color='darkblue', label='Downregulated', edgecolors='black', linewidths=1)
plt.axvline(x=fold_change_threshold, color='gray', linestyle='--')
plt.axvline(x=-fold_change_threshold, color='gray', linestyle='--')
plt.axhline(y=-np.log10(p_value_threshold), color='gray', linestyle='--')
plt.xlabel('log2(Fold Change)')
plt.ylabel('-log10(p-value)')
# plt.title('Volcano Plot')

# 为显著变化的基因添加标签
texts = []
for i in significantly_upregulated.index:
    texts.append(plt.text(significantly_upregulated.loc[i, 'Fold Change'],
                          -np.log10(significantly_upregulated.loc[i, 'p-value']),
                          pathway_names[i], color='red'))
for i in significantly_downregulated.index:
    texts.append(plt.text(significantly_downregulated.loc[i, 'Fold Change'],
                          -np.log10(significantly_downregulated.loc[i, 'p-value']),
                          pathway_names[i], color='blue'))

# 调整标签位置，避免重叠
adjust_text(texts)
# adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

plt.legend(loc='lower right')
plt.savefig("/Users/ben/Documents/CDD/IBS/humann3_out/火山图.png",dpi=300)
plt.show()
