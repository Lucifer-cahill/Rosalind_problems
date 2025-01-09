
data = open('ID_DNA\\rosalind_dna.txt').read()
def count_nt(str):
    count = {nt : 0 for nt in 'ATGC'}
    for i in str[:-1]:
        if i in 'ACGT':
            count[i] +=1

    return count
output = list(count_nt(data).values())

output = ' '.join([str(x) for x in output])
with open('ID_DNA\\DNA_output.txt', 'w') as f:
        f.write(output)
