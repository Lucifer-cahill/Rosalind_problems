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

Poss_mRNA = {}

for i in RNA_cod_table:
    if RNA_cod_table[i] not in Poss_mRNA:
        Poss_mRNA[RNA_cod_table[i]] = 1
    else:
        Poss_mRNA[RNA_cod_table[i]] += 1


data = open('rosalind_mrna.txt').read()
output = 1
for i in data:
    if i == '\n':
        continue
    output = Poss_mRNA[i]*output
output = output*3
print(output)
print(output%1000000)



    