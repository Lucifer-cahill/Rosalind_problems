data = open('rosalind_hamm.txt').read()
dna_s = ''
dna_t = ''
flag = False
for i in data:
    if i == '\n':
        flag = True
    if not flag:
        dna_s = dna_s + i
    else:
        if i != '\n':
            dna_t = dna_t + i
# print(dna_s)
# print(dna_t)
count = 0
for i in range(len(dna_s)):
    if dna_s[i] != dna_t[i]:
        count += 1

print(count)


     




