import pandas as pd

data = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/FC_data_group/FC_IBS_HC_normed_4Aug2023.csv', index_col=0)

# 读取Responder和Non-responder信息
responder_samples = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/responder_samples.csv')['sample'].tolist()
non_responder_samples = pd.read_csv('/Users/ben/Documents/CDD/Functional_Constipation/non_responder_samples.csv')['sample'].tolist()

# 剔除不属于Responder或Non-responder的样本

selected_samples = responder_samples + non_responder_samples

data = data[selected_samples]

data.to_csv('/Users/ben/Documents/CDD/Functional_Constipation/FC_MZRW_Week4.csv')