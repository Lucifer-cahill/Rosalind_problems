from Bio.Seq import Seq
from Bio import SeqIO
for seq_data in SeqIO.parse('ID_ORF\\rosalind_orf.txt','fasta'):
    seq = seq_data.seq
# seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
print(seq)
seq_1 = Seq(seq)

cod_mrna = seq_1.transcribe()
tem_mrna = seq_1.reverse_complement().transcribe()


orf_lst = []
for seq_temp in [cod_mrna,tem_mrna]:
    for i in range(3):
        temp_orf = ''
        seq = seq_temp[i:]
        while len(seq) % 3 != 0:
            seq += 'N' 

        flag = False
        for i in seq.translate():
            if i == '*':
                if temp_orf:
                    orf_lst.append(temp_orf)
                    temp_orf = ''
                flag = False                
            if i == 'M' or flag:
                temp_orf += i
                flag = True
in_orf_lst = []
for orf in orf_lst:
    for i in range(1,len(orf)):
        if orf[i] == 'M':
            in_orf_lst.append(orf[i:])
orf_lst = orf_lst + in_orf_lst


output = '\n'.join(set(orf_lst))



# print(output, len(in_orf_lst))


with open('ID_ORF\\ORF_output.txt', 'w') as f:
        f.write(output)

