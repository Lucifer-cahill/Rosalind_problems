import math
from Bio.Seq import Seq
from Bio import SeqIO
# data = open('ID_LONG\\rosalind_long.txt').read()
data = open('sample.txt').read()
seq_dict = {}
for seq_data in SeqIO.parse('ID_PMCH\\rosalind_pmch.txt','fasta'):
    # seq_dict[seq_data.id] = str(seq_data.seq)
    rna_seq = str(seq_data.seq)
nt_count = {nt: 0 for nt in 'AGCU'}
for nt in rna_seq:
    nt_count[nt] += 1

perf_match = math.factorial(nt_count['A'])*math.factorial(nt_count['G'])
print(nt_count)
print(perf_match)

# output = ' '.join([str(x) for x in output])
# with open('PMCH_output.txt', 'w') as f:
#         f.write(output)

