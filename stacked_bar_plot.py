import pandas as pd
import matplotlib.pyplot as plt
import os

# 读取CSV文件
def read_csv(filename):
    data = pd.read_csv(filename, index_col=0)
    return data

# 获取每组的top物种标签
def get_top_labels(data, n):
    labels = data.sum().sort_values(ascending=False).index[:n]
    return labels

# 将不在top物种中的物种标记为"Other"
def label_as_other(data, labels):
    data.loc[~data.index.isin(labels), 'Other'] = data.loc[~data.index.isin(labels)].sum(axis=1)
    data = data[labels.tolist() + ['Other']]
    return data

# 绘制堆叠图
def plot_stacked_bar(data, sample_names):
    fig, ax = plt.subplots()
    ax.stackplot(sample_names, data.values.T, labels=data.columns)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('Samples')
    plt.ylabel('Relative Abundance')
    plt.title('Species Composition')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 主函数
def main():
    # 读取CSV文件
    filenames = ['genus_MZRW_baseline_group_metaphlan_normed.csv', 'genus_MZRW_week4_group_metaphlan_normed.csv', 'genus_Placebo_baseline_group_metaphlan_normed.csv', 'genus_Placebo_week4_group_metaphlan_normed.csv']
    group_names = ['MZRW_baseline', 'MZRW_week4', 'Placebo_baseline', 'Placebo_week4']
    top_n = 20  # 取前20个物种

    for filename, group_name in zip(filenames, group_names):
        # 从CSV文件中读取数据
        data = read_csv(filename)

        # 获取前N个物种的标签
        top_labels = get_top_labels(data, top_n)

        # 将不在前N个物种中的物种标记为"Other"
        labeled_data = label_as_other(data, top_labels)

        # 绘制堆叠图
        plot_stacked_bar(labeled_data, data.columns)

        # 输出组别名称
        print(f"Group: {group_name}\n")

if __name__ == '__main__':
    os.chdir("/Users/ben/Documents/CDD/IBS/IBS-C_data/processed")
    main()