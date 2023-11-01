import os
import re
import pandas as pd
def read_cluster_file(cluster_file):
    infos = []
    with open(cluster_file, 'r') as f:
        lines = f.readlines()
        count =''
        representative_id = None
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                # 处理上一个cluster
                if representative_id is not None and count != '':
                    infos.append((representative_id, count))
                # 开始新的cluster
                representative_id = None
                count = ''
            else:
                count = int(line.strip().split('\t')[0]) + 1
                if "*" in line:
                    representative_id = re.split(r'[>.]',line,maxsplit=2)[1]
        # 处理最后一个cluster
        if representative_id is not None and count != '':
            infos.append((representative_id, count))
    return infos

result = pd.DataFrame()
for root, dirs, files in os.walk("/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/cd-hit"):
    for file in files:
        file_path = os.path.join(root, file)
        # 在这里对文件进行操作，例如打印文件路径
        if file.endswith("fasta.clstr"):
            cluster_info = read_cluster_file(file_path)
            df = pd.DataFrame(cluster_info)
            result = pd.concat([result,df])
result.to_csv('/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/cluster_info.csv',index=False, header=['representative id','count'])


