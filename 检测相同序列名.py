import csv
import os
import re

def read_fasta_files(directory):
    sequences = {}
    for filename in os.listdir(directory):
        if filename.endswith('.fasta'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as fasta_file:
                sequence_name = ''
                for line in fasta_file:
                    line = line.strip()
                    if line.startswith('>'):
                        if sequence_name:
                            sequences.setdefault(sequence_name, set()).add(filename)
                        sequence_name = re.split(r'[>#]', line, maxsplit=2)[1].strip()
                    elif line.startswith('#'):
                        break
                if sequence_name:
                    sequences.setdefault(sequence_name, set()).add(filename)
    return sequences

def find_sequences_with_same_names(sequences):
    common_sequences = {}
    for sequence_name, filenames in sequences.items():
        if len(filenames) > 1:
            common_sequences[sequence_name] = filenames
    return common_sequences

# 示例用法
directory = '/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/smorf_cluster_seq'  # 替换为包含 FASTA 文件的目录路径
sequences = read_fasta_files(directory)
common_sequences = find_sequences_with_same_names(sequences)

# 将信息保存到 CSV 文件
csv_file = '/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/duplicate_sequences.csv'  # CSV 文件路径

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sequence ID', 'File Names'])

    for sequence_name, filenames in common_sequences.items():
        writer.writerow([sequence_name, ', '.join(filenames)])

print('CSV 文件保存成功: ', csv_file)