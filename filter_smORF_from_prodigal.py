import os

def read_fasta_file(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = None
        sequence = ''
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                # 处理上一个序列
                if header is not None and sequence != '':
                    sequences.append((header, sequence))
                # 开始新的序列
                header = line
                sequence = ''
            else:
                sequence += line
        # 处理最后一个序列
        if header is not None and sequence != '':
            sequences.append((header, sequence))
    return sequences
def filter_sequences(sequences):
    filtered_sequences = []
    for header, sequence in sequences:
        # 解析序列header中的信息
        header_parts = header.split('#')
        start_type = header_parts[-1].strip().split(';')[2].split('=')[-1]
        first_num = int(header_parts[1].strip())
        second_num = int(header_parts[2].strip())
        # 根据条件筛选序列
        if not start_type == 'Edge' and (second_num - first_num) <= 151:
            filtered_sequences.append((header, sequence))
            print(start_type)
            print(second_num - first_num)
    return filtered_sequences

for root, dirs, files in os.walk("/Users/ben/Documents/CDD/IBS/ibs_c_final/smORF/cd-hit_out"):
    for file in files:
        file_path = os.path.join(root, file)
        # 在这里对文件进行操作，例如打印文件路径
        if file.endswith(".cluster.fasta"):
            filtered_sequences = filter_sequences(read_fasta_file(file_path))
            new_name = file.split('.')[0] + "_smORF.fasta"
            with open('/Users/ben/Documents/CDD/IBS/ibs_c_final/smORF/cd-hit_filtered/' + new_name,'w') as f:
                for header, sequence in filtered_sequences:
                    f.writelines(header)
                    f.writelines("\n")
                    f.writelines(sequence)
                    f.writelines("\n")
                f.close()


