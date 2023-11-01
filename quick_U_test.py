from scipy.stats import mannwhitneyu

responder_list = []
with open("/Users/ben/Desktop/responder.txt") as f:
    for line in f.readlines():
        responder_list.append(float(line.strip("\n")))

non_responder_list = []
with open("/Users/ben/Desktop/non_responder.txt") as f:
    for line in f.readlines():
        non_responder_list.append(float(line.strip("\n")))

t_stat, p_value = mannwhitneyu( responder_list,non_responder_list,alternative="two-sided")
print(p_value)