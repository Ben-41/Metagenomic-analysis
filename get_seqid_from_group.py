import os
import re
import pandas as pd

def get_seqid(input_path,sample_group,output_file):

    MZRW_baseline_list = []
    MZRW_week_4_list = []
    Placebo_baseline_list = []
    Placebo_week_4_list = []

    CSBM_responder_list = []
    CSBM_non_responder_list = []

    group = pd.read_csv(sample_group)

    MZRW_baseline = group[group["Class"] == "MZRW_baseline"]['sample']
    MZRW_week_4 = group[group["Class"] == "MZRW_week_4"]['sample']
    Placebo_baseline = group[group["Class"] == "Placebo_baseline"]['sample']
    Placebo_week_4 = group[group["Class"] == "Placebo_week_4"]['sample']

    CSBM_responder = group[group["Class"] == "responder"]['sample']
    CSBM_non_responder = group[group["Class"] == "non_responder"]['sample']

    for root, dirs, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 在这里对文件进行操作，例如打印文件路径
            if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in CSBM_responder):
                with open(file_path,"r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('>'):
                            line = line.strip()
                            CSBM_responder_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
                            CSBM_responder_list.append(CSBM_responder_contig_id)

    for root, dirs, files in os.walk(input_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 在这里对文件进行操作，例如打印文件路径
            if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in CSBM_non_responder):
                with open(file_path,"r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('>'):
                            line = line.strip()
                            CSBM_non_responder_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
                            CSBM_non_responder_list.append(CSBM_non_responder_contig_id)

    # for root, dirs, files in os.walk(input_path):
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         # 在这里对文件进行操作，例如打印文件路径
    #         if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in MZRW_baseline):
    #             with open(file_path,"r") as f:
    #                 lines = f.readlines()
    #                 for line in lines:
    #                     if line.startswith('>'):
    #                         line = line.strip()
    #                         MZRW_baseline_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
    #                         MZRW_baseline_list.append(MZRW_baseline_contig_id)
    #
    #         if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in MZRW_week_4):
    #             with open(file_path,"r") as f:
    #                 lines = f.readlines()
    #                 for line in lines:
    #                     if line.startswith('>'):
    #                         MZRW_week_4_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
    #                         MZRW_week_4_list.append(MZRW_week_4_contig_id)
    #
    #         if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in Placebo_baseline):
    #             with open(file_path,"r") as f:
    #                 line = line.strip()
    #                 lines = f.readlines()
    #                 for line in lines:
    #                     if line.startswith('>'):
    #                         Placebo_baseline_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
    #                         Placebo_baseline_list.append(Placebo_baseline_contig_id)
    #
    #         if file.endswith("smORF.fasta") and any(file.startswith(sample_id) for sample_id in Placebo_week_4):
    #             with open(file_path,"r") as f:
    #                 line = line.strip()
    #                 lines = f.readlines()
    #                 for line in lines:
    #                     if line.startswith('>'):
    #                         Placebo_week_4_contig_id = re.split(r'[>#]', line, maxsplit=2)[1].strip() + "_0"
    #                         Placebo_week_4_list.append(Placebo_week_4_contig_id)

    data = {'CSBM_responder': pd.Series(CSBM_responder_list),
            'CSBM_non_responder': pd.Series(CSBM_non_responder_list)}

    # data = {'MZRW_baseline': pd.Series(MZRW_baseline_list),
    #         'MZRW_week_4': pd.Series(MZRW_week_4_list),
    #         'Placebo_baseline': pd.Series(Placebo_baseline_list),
    #         'Placebo_week_4': pd.Series(Placebo_week_4_list)}

    # data = {'MZRW_baseline': pd.Series(list(set(MZRW_baseline_list))),
    # 'MZRW_week_4': pd.Series(list(set(MZRW_week_4_list))),
    # 'Placebo_baseline': pd.Series(list(set(Placebo_baseline_list))),
    # 'Placebo_week_4': pd.Series(list(set(Placebo_week_4_list)))}

    df = pd.DataFrame(data)
    df.to_csv(output_file)

get_seqid('/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/smorf_cluster_seq',"/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/ibs_c_responder_group.csv"
          ,'/Users/ben/Documents/CDD/2101/IBS/ibs_c_final/smORF/contigs分组信息_1.csv')

