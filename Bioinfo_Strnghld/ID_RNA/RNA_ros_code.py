# str = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
data = open('rosalind_rna.txt').read()

output = ''

for i in range(len(data)):
    if data[i] == 'T':
        output += 'U'
    else:
        output += data[i]

print(output)
