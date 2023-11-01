import pandas as pd

species_data = pd.read_csv("/Users/ben/Documents/CDD/2101/biomarker_ibs_fc/fc_ibs_c_metaphlan_merged.csv", index_col= 0)
group_data = pd.read_csv("/Users/ben/Documents/CDD/2101/biomarker_ibs_fc/ibs_c_fc_baseline_group.csv", index_col=1)

## 通过index：四个对照组和sample id，查找具体的行
# MZRW_baseline_group = species_data.loc[:, group_data.loc['MZRW_baseline', 'sample']]
# MZRW_week_4_group = species_data.loc[:, group_data.loc['MZRW_week_4', 'sample']]
# Placebo_baseline_group = species_data.loc[:, group_data.loc['Placebo_baseline', 'sample']]
# Placebo_week_4_group = species_data.loc[:, group_data.loc['Placebo_week_4', 'sample']]
# MZRW_responder_group = species_data.loc[:, group_data.loc['responder', 'sample']]
# MZRW_non_responder_group = species_data.loc[:, group_data.loc['non_responder', 'sample']]
ibs_c_baseline_group = species_data.loc[:, group_data.loc['IBS-C_baseline', 'sample']]
fc_baseline_group = species_data.loc[:, group_data.loc['FC_baseline', 'sample']]


## 将结果合并回来
# merge_df = pd.concat([MZRW_baseline_group, MZRW_week_4_group, Placebo_baseline_group, Placebo_week_4_group], axis=1, ignore_index=False)
# merge_df = pd.concat([MZRW_responder_group,MZRW_non_responder_group],axis=1, ignore_index=False)
# merge_df.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/lefse/ibs_c_species_norm_responder_lefse.csv")
merge_df = pd.concat([ibs_c_baseline_group,fc_baseline_group],axis=1,ignore_index=False)
merge_df.to_csv("/Users/ben/Documents/CDD/2101/biomarker_ibs_fc/ibs_c_fc_baseline_metaphlan_norm.csv")
## 将结果分别输出
# MZRW_baseline_group.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_baseline_group_normed.csv")
# MZRW_week_4_group.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_week_4_group_normed.csv")
# Placebo_baseline_group.to_csv("/Users/ben/Documents/CDD/IBS/IBS-C_data/processed/genus_Placebo_baseline_group_metaphlan_normed.csv")
# Placebo_week_4_group.to_csv("/Users/ben/Documents/CDD/IBS/IBS-C_data/processed/genus_Placebo_week4_group_metaphlan_normed.csv")
# MZRW_responder_group.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_responder_group_normed.csv")
# MZRW_non_responder_group.to_csv("/Users/ben/Documents/CDD/IBS/ibs_c_final/u_test/MZRW_non_responder_group_normed.csv")
