data = open('rosalind_orf (4).txt').read()
data = ''.join(data.split('\n')[1:])
output = ''

for i in range(len(data)):
    if data[i] == 'T':
        output += 'U'
    else:
        output += data[i]
print(output)

comp = {'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'}
output_revc = ''
for i in data:
    if i in comp:
        output_revc = comp[i] + output_revc
# print(output_revc)

revc_mrna = ''
for i in range(len(output_revc)):
    if output_revc[i] == 'T':
        revc_mrna += 'U'
    else:
        revc_mrna += output_revc[i]
print(revc_mrna)

cod_table = open('codon_table.txt').read()
RNA_cod_table = {}
codon = ''
for i in cod_table:
    if not codon and i == ' ':
        continue
    if len(codon) < 5:
        codon = codon + i
    else:
        RNA_cod_table[codon[0:3]] = codon[4]
        codon = ''

prot_str = ''
codon = ''
# flag = False
# for i in range(len(output[:-3])):
#     if output[i:i+3] == 'AUG' and not flag:
#         prot_str = 'M'
#         flag = True
#     if flag:
#         codon = codon + output[i+3]
#         if len(codon) == 3: 
#             # print(codon) 
#             if codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
#                 print(prot_str)
#                 while 'M' in prot_str[1:]:
#                     prot_str = prot_str[1:]
#                     prot_str = prot_str[prot_str.find('M'):]
#                     print(prot_str)

#                 prot_str = ''
#                 flag = False
#                 codon = ''
#             else:
#                 prot_str = prot_str + RNA_cod_table[codon]
#                 codon = ''

for i in range(len(output[:-2])):
    if output[i:i+3] == 'AUG':
        prot_str = 'M'
        read_frame = output[i+3:]
        for j in range(len(read_frame)):         
            codon = codon + read_frame[j]
            if len(codon) == 3: 
                # print(codon) 
                if codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
                    print(prot_str)
                    prot_str = ''
                    codon = ''
                    break
                else:
                    prot_str = prot_str + RNA_cod_table[codon]
                    codon = ''

for i in range(len(revc_mrna[:-2])):
    if revc_mrna[i:i+3] == 'AUG':
        prot_str = 'M'
        read_frame = revc_mrna[i+3:]
        for j in range(len(read_frame)):         
            codon = codon + read_frame[j]
            if len(codon) == 3: 
                # print(codon) 
                if codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
                    print(prot_str)
                    prot_str = ''
                    codon = ''
                    break
                else:
                    prot_str = prot_str + RNA_cod_table[codon]
                    codon = ''
print('\n')