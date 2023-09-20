import csv
from scipy.stats import mannwhitneyu
import pandas as pd
import numpy as np

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)
    return rows

def read_txt_file(filename):
    samplelist = []
    with open(filename,'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for line in lines:
            samplelist.append(line)
    return samplelist

def get_sample_groups(rows,sample_list):
    sample_groups = {'control': [], 'experimental': []}
    sample_names = rows[0][1:]

    for row in rows[1:]:
        pathway_name = row[0]
        for i, sample_value in enumerate(row[1:]):
            sample_name = sample_names[i]
            if sample_name in sample_list:
                if sample_name.endswith('_1a'):
                    sample_groups['control'].append((pathway_name, sample_name, sample_value))
                elif sample_name.endswith('_3a'):
                    sample_groups['experimental'].append((pathway_name, sample_name, sample_value))
                elif sample_name.endswith('_1b'):
                    sample_groups['control'].append((pathway_name, sample_name, sample_value))
                elif sample_name.endswith('_3b'):
                    sample_groups['experimental'].append((pathway_name, sample_name, sample_value))
                elif sample_name.endswith('_3c'):
                    sample_groups['experimental'].append((pathway_name, sample_name, sample_value))
    # print(len(sample_groups["experimental"]))

    return sample_groups

def FC(group1,group2):
    global fold_change
    control_group = np.array([group1])
    experimental_group = np.array([group2])
    control_group_mean = np.mean(control_group)
    experimental_group_mean = np.mean(experimental_group)

    if experimental_group_mean != 0 and control_group_mean != 0:
        fold_change = np.log2(experimental_group_mean / control_group_mean)
    elif experimental_group_mean == 0 and control_group_mean != 0:
        experimental_group_mean = 1e-8
        fold_change = np.log2(experimental_group_mean / control_group_mean)
    elif control_group_mean == 0 and experimental_group_mean != 0:
        control_group_mean = 1e-8
        fold_change = np.log2(experimental_group_mean / control_group_mean)
    elif control_group_mean == 0 and experimental_group_mean == 0:
        control_group_mean = 1e-8
        experimental_group_mean = 1e-8
        fold_change = np.log2(experimental_group_mean / control_group_mean)

    return fold_change

def U_test(group1,group2):
    statistic, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    return p_value

if __name__ == "__main__":

    # 读取CSV文件,第一行为sample title，第一列为pathway，数据为相对丰度
    filename = '/Users/ben/Documents/CDD/IBS/humann3_out/FC_unstratified_DATA.csv'  # 替换为你的CSV文件路径
    data = read_csv_file(filename)

    # 获取样本列表
    sample_list = read_txt_file("/Users/ben/Documents/CDD/IBS/humann3_out/FC_treatment_list.txt")

    # 获取样本分组信息，这里分为实验组和对照组
    sample_groups = get_sample_groups(data,sample_list)

    # 获得每组每个pathway的数据

    pathway_value_control = {}
    pathway_value_experimental = {}

    k = []
    j =[]
    for group in sample_groups["control"]:
        if group[1] in sample_list and group[1] not in k:
            k.append(group[1])
    print(len(k))
    print("control sample counts:", k)

    for group in sample_groups["experimental"]:
        if group[1] in sample_list and group[1] not in j:
            j.append(group[1])
    print(len(j))
    print("experimental sample counts:", j)

    for group in sample_groups["control"]:
        if group[1] in sample_list:
            if group[0] in pathway_value_control:
                pathway_value_control[group[0]].append(float(group[2]))
            else:
                pathway_value_control[group[0]] = []
                pathway_value_control[group[0]].append(float(group[2]))

    for group in sample_groups["experimental"]:
        if group[1] in sample_list:
            if group[0] in pathway_value_experimental:
                pathway_value_experimental[group[0]].append(float(group[2]))
            else:
                pathway_value_experimental[group[0]] = []
                pathway_value_experimental[group[0]].append(float(group[2]))


    # 计算P-value 和 计算Fold-changes
    result_lists = []
    for pathway in pathway_value_control.keys():
        result_list = []
        pvalue = U_test(pathway_value_control[pathway], pathway_value_experimental[pathway])
        fold_change = FC(pathway_value_control[pathway],pathway_value_experimental[pathway])
        result_list.append(pathway)
        result_list.append(pvalue)
        result_list.append(fold_change)
        result_lists.append(result_list)
    # print(result_lists)
    #导出
    df = pd.DataFrame(result_lists)
    df.to_csv("/Users/ben/Documents/CDD/IBS/humann3_out/u-test.csv")



    for pathway in pathway_value_control.keys():
        p_value = U_test(pathway_value_control[pathway], pathway_value_experimental[pathway])

    sample_experimental = []
    sample_control = []
    for sample in sample_groups["experimental"]:
        if sample[1] not in sample_experimental:
            sample_experimental.append(sample)

    for sample in sample_groups["control"]:
        if sample[1] not in sample_control:
            sample_control.append(sample)

    # print("Experimental sample: ",len(sample_experimental))
    # print("Control sample: ", len(sample_control))
    # # 打印结果
    # print('对照组:')
    # for pathway_name, sample_name, sample_value in sample_groups['control']:
    #     print('Pathway:', pathway_name, 'Sample:', sample_name, 'Value:', sample_value)
    #
    # print('实验组:')
    # for pathway_name, sample_name, sample_value in sample_groups['experimental']:
    #     print('Pathway:', pathway_name, 'Sample:', sample_name, 'Value:', sample_value)

