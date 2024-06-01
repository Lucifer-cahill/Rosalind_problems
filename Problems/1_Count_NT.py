
data = open('rosalind_dna.txt').read()

count = {nt : 0 for nt in 'ATGC'}

for i in data[:-1]:
    count[i] +=1

print(*count.values())
