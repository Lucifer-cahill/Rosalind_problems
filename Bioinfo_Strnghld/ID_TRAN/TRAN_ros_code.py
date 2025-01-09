from Bio.Seq import Seq
from Bio import SeqIO
# data = open('ID_TRAN\\rosalind_tran.txt').read()
# data = open('sample.txt').read()
seq_lst = []
for seq_data in SeqIO.parse('ID_TRAN\\rosalind_tran.txt','fasta'):
    seq_lst.append(str(seq_data.seq))

transitions = {'A': 'G',
               'G': 'A',
               'C': 'T',
               'T': 'C'}

transversions = {'A': ['C','T'],
                 'G': ['C','T'],
                 'C': ['G','A'],
                 'T': ['G','A']}
n_ver = 0 
n_sit = 0

for i in range(len(seq_lst[0])):
    if seq_lst[0][i] == seq_lst[1][i]:
        continue
    if seq_lst[1][i] == transitions[seq_lst[0][i]]:
        n_sit += 1
    if seq_lst[1][i] in transversions[seq_lst[0][i]]:
        n_ver += 1

print(n_sit/n_ver)
    




# output = ' '.join([str(x) for x in output])
# with open('LGIS_output.txt', 'w') as f:
#         f.write(output)
