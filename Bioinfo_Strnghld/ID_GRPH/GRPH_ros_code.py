data = open('rosalind_grph.txt').read()
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
# print(str_dict)

for i in str_dict:
    for j in str_dict:
        if str_dict[i][-3:] == str_dict[j][:3] and i != j:
            print(i,j)  
  
