import pandas as pd
import os

##########合并kraken文件

# 定义合并后的文件名
merged_filename = "/Users/ben/Documents/CDD/IBS/ibs_c_final/methanogen/合并文件.csv"


# 遍历文件夹中的所有文件
folder_path = "/Users/ben/Documents/CDD/IBS/ibs_c_final/methanogen"  # 替换为实际的文件夹路径

k = 0

header = ['']
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    header.append(filename)
    # 读取文件内容
    df_1 = pd.read_csv(folder_path+"/"+filename,delimiter="\t")
    if k==0:
        merged_df = df_1
        k+=1
    else:
        merged_df = pd.merge(df_1,merged_df,left_on=df_1.columns[0], right_on=merged_df.columns[0], how='outer')

merged_df = merged_df.fillna(0)
merged_df.loc[-1] = header
merged_df.index = merged_df.index + 1
merged_df = merged_df.sort_index()
# merged_df_final = pd.concat([pd.DataFrame([header], columns=merged_df.columns), merged_df], ignore_index=True)
# 保存合并后的DataFrame为txt文件
merged_df.to_csv(merged_filename)

############################END##############################



# # 读取第一个表格
# df1 = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/FC_data_group/FC_IBS_HC_normed_4Aug2023.csv')
# # 读取第二个表格
# df2 = pd.read_csv('/Users/ben/Documents/CDD/IBS/ibs_c_final/IBS_C_normed_6Oct2023.csv')
#
# # 合并两个表格，将物种名称作为键
# merged_df = pd.merge(df1, df2, on='species', how='outer')
#
# # 如果某个物种在一个表格中存在，在另一个表格中不存在，对应的单元格会填充为NaN
# # 您可以根据需要进行进一步的处理，例如填充缺失值
# merged_df = merged_df.fillna(0)
#
# # 输出合并后的表格
# merged_df.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/fc_hc_ibs_c_metaphlan_merged.csv")