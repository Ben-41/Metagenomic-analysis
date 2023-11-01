import pandas as pd

data = pd.read_csv('/Users/ben/Documents/CDD/动物实验/Shujun_metaphlan_merged_table.csv') # 如果文件以制表符分隔，使用 delimiter='\t'
# print(data['clade_name'].str.split('|').str[-1].str.startswith('g'))
filtered_data = data[data['clade_name'].str.split('|').str[-1].str.startswith('s')]
new_index = filtered_data.iloc[:, 0].str.split('|').str[-1] # 拆分第一列的字符串，并获取最后一部分作为新的行名
# new_index = new_index.str.split('_', n=2).str[-1] # 删除新行名中最后一个 "_" 之前的内容
filtered_data.index = new_index
filtered_data.to_csv('/Users/ben/Documents/CDD/动物实验/lefse/Shujun_metaphlan_species.csv')

