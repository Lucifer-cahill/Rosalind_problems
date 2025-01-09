# data = open('rosalind_subs.txt').read()
# dna_s = ''
# dna_t = ''
# flag = False
# for i in data:
#     if i == '\n':
#         flag = True
#     if not flag:
#         dna_s = dna_s + i
#     else:
#         if i != '\n':
#             dna_t = dna_t + i

dna_s = 'GATATATGCATATACTT'
dna_t = 'ATAT'
output = []
for i in range(len(dna_s)-len(dna_t)):
    for j in range(len(dna_t)):
        if dna_s[i+j] == dna_t[j]:
            flag = True
        else:
            flag = False 
            break
    if flag:
        output.append(i+1)
output_str = ''
for i in output:
    output_str = output_str + str(i) + ' '

print(output_str)




