data = open('rosalind_prot(1).txt').read()
# data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
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
    
print(RNA_cod_table)

prot_str = ''
for i in data:
    codon = codon + i
    if len(codon) == 3:  
        if codon == 'UGA' or codon == 'UAA' or codon == 'UAG':
            break
        else:
            prot_str = prot_str + RNA_cod_table[codon]
            codon = ''

with open('RNA2Prot_output.txt', 'w') as f:
        f.write(prot_str)
# print(prot_str)
    