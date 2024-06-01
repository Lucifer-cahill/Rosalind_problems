# str = 'AGCTTTTCATTCTGACTGCAA'
data = open('rosalind_gc.txt').readlines()
print(data)
str_dict = {}
dnaid = '' 
dnant = ''

for i in data:
    if i == '>':
        str_dict[dnaid[1:]] = dnant
        dnaid = ''
        dnant = ''
        flag = True
    if i == '\n':
        flag = False
    if flag:
        dnaid = dnaid + i
    else:
        if i != '\n':
            dnant = dnant + i
str_dict[dnaid[1:]] = dnant
str_dict.pop('')
max = 0
for key in str_dict:
    count_GC = 0
    GC_cont = 0
    for i in str_dict[key]:
        if i == 'G' or i == 'C':
            count_GC += 1
    GC_cont = count_GC*100/len(str_dict[key])
    str_dict.update({key : GC_cont})
    if GC_cont > max:
        max = GC_cont
        max_key = key
print(str_dict)
print(max_key)
print(max)

