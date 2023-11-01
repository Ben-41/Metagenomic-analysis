import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

# 读取CSV文件
df = pd.read_csv('/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_responder_group_normed.csv', index_col=0)

# 分割组名和样本数据
group1_name = 'Group1'  # 假设组名为Group1
group1_data = df.copy()

# 读取另一个组的CSV文件
df2 = pd.read_csv('/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_non_responder_group_normed.csv', index_col=0)

# 分割组名和样本数据
group2_name = 'Group2'  # 假设组名为Group2
group2_data = df2.copy()

# 给列表中为0的值添加一个极小值
# group1_data[group1_data == 0] = 1e-8
# group2_data[group2_data == 0] = 1e-8

# 执行差异分析（这里使用独立双样本t检验作为示例）
p_values = []
fold_changes = []
for species in df.index:
    fold_change = np.mean(group1_data.loc[species]) / np.mean(group2_data.loc[species])
    t_stat, p_value = mannwhitneyu(group1_data.loc[species], group2_data.loc[species], alternative="two-sided")
    fold_changes.append(fold_change)
    p_values.append(p_value)


# 多重检验校正（这里使用Benjamini-Hochberg方法）
adjusted_p_values = np.array(p_values)
adjusted_p_values *= len(adjusted_p_values)  # 使用Bonferroni校正
adjusted_p_values = np.minimum(adjusted_p_values, 1)  # 限制校正后的p值不超过1

# 创建结果DataFrame
result = pd.DataFrame({
    'Species': df.index,
    'FoldChange': fold_changes,
    'PValue': p_values,
    'AdjustedPValue': adjusted_p_values
})


# 打印结果
print(result)
result.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_responder_nonresponder_Pvalue.csv")