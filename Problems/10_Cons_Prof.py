data = open('rosalind_cons.txt').read()
# print(data)
str_dict = {}
dnaid = '' 
dnant = ''
lst = []
profile = []
for i in data:
    if i == '>':
        str_dict[dnaid[1:]] = dnant
        dnaid = ''
        dnant = ''
        profile.append(lst)
        lst = []
        flag = True
    if i == '\n':
        flag = False
    if flag:
        dnaid = dnaid + i
    else:
        if i != '\n':
            dnant = dnant + i
            lst.append(0)
str_dict[dnaid[1:]] = dnant
str_dict.pop('')
profile.pop(0)

for i in str_dict:
    for j in range(len(str_dict[i])):
        if str_dict[i][j] == 'A':
            profile[0][j] += 1
        elif str_dict[i][j] == 'C':
            profile[1][j] += 1
        elif str_dict[i][j] == 'G':
            profile[2][j] += 1
        elif str_dict[i][j] == 'T':
            profile[3][j] += 1 

# print(profile)  
consensus = ''
for j in range(len(profile[0])):
    smlst = [row[j] for row in profile]
    idx = smlst.index(max(smlst))
    if idx == 0:
        consensus += 'A' 
    if idx == 1:
        consensus += 'C' 
    if idx == 2:
        consensus += 'G' 
    if idx == 3:
        consensus += 'T' 
consensus += '\n'


prof_str = ''
prof_str += 'A: '
for i in range(len(profile[0])):
    prof_str += str(profile[0][i]) + ' '
prof_str += '\n'
prof_str += 'C: '
for i in range(len(profile[0])):
    prof_str += str(profile[1][i]) + ' '
prof_str += '\n'
prof_str += 'G: '
for i in range(len(profile[0])):
    prof_str += str(profile[2][i]) + ' '
prof_str += '\n'
prof_str += 'T: '
for i in range(len(profile[0])):
    prof_str += str(profile[3][i]) + ' '
prof_str += '\n'

    
with open('10_cons_output.txt', 'w') as f:
        f.write(consensus)
        f.write(prof_str)




