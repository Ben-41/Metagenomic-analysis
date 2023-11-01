
file_1 = open("/Users/ben/Documents/CDD/linux_script/list_ibs_c.txt", 'r')
file_2 = open("/Users/ben/Documents/CDD/linux_script/list_ibs_c_1.txt", 'r')

l1 = []
for line in file_2.readlines():
    line.strip('\n')
    l1.append(line)
for line in file_1.readlines():
    if line not in l1:
        print(line)
