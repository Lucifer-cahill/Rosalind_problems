data = open('rosalind_hamm.txt').read()
input = data.split('\n')
dna_s = input[0]
dna_t = input[1]

count = 0
for i in range(len(dna_s)):
    if dna_s[i] != dna_t[i]:
        count += 1

print(count)


     




