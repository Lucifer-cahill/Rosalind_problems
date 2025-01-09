from Bio.Seq import Seq
from Bio import SeqIO
# # data = open('ID_LONG\\rosalind_long.txt').read()
# data = open('sample.txt').read()
seq_lst = []
for seq_data in SeqIO.parse('ID_SSEQ\\rosalind_sseq.txt','fasta'):
    seq_lst.append(str(seq_data.seq))

ind_lst = []
k = 0
for j in range(len(seq_lst[0])):
    if seq_lst[0][j] == seq_lst[1][k]:
        ind_lst.append(j+1)
        k += 1
    if k == len(seq_lst[1]):
        break

print(ind_lst)


output = ' '.join([str(x) for x in ind_lst])
with open('ID_SSEQ\\SSEQ_output.txt', 'w') as f:
        f.write(output)