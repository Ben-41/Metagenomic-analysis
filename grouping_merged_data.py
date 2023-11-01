import pandas as pd

# 读取Excel表格1
df1 = pd.read_excel('/Users/ben/Documents/CDD/Functional_Constipation/Responsder2patient.xlsx')

# 读取Excel表格2
df2 = pd.read_excel('/Users/ben/Documents/CDD/Functional_Constipation/sample2patient.xlsx')

# 提取Responder的sample名
responder_samples = df2[df2['patient'].isin(df1[df1['CSBM_responsder'] == 'Responsder']['patient'])]['sample'].tolist()

# 提取Non_responder的sample名
non_responder_samples = df2[df2['patient'].isin(df1[df1['CSBM_responsder'] == 'Non_responsder']['patient'])]['sample'].tolist()
# 输出到文件夹
responder_df = pd.DataFrame({'sample': responder_samples})
non_responder_df = pd.DataFrame({'sample': non_responder_samples})

responder_df.to_csv('/Users/ben/Documents/CDD/Functional_Constipation/responder_samples.csv', index=False)
non_responder_df.to_csv('/Users/ben/Documents/CDD/Functional_Constipation/non_responder_samples.csv', index=False)
# 打印结果
print('Responder samples:')
print(responder_samples)
print('Non-responder samples:')
print(non_responder_samples)