from Bio.Seq import Seq
from Bio import SeqIO

a = "abcdefgh"
b = "efg"

print(a.index(b))

introns = {}
for seq_data in SeqIO.parse('ID_SPLC\\rosalind_splc.txt','fasta'):
    introns[seq_data.id] = str(seq_data.seq)
dna_s = list(introns.values())[0]
print(dna_s)
del introns[list(introns.keys())[0]]
spliced_form = ''
for id in introns:
    sub_ind = dna_s.index(introns[id])
    spliced_form = dna_s[:sub_ind] + dna_s[(sub_ind+len(introns[id])):]  
    dna_s = spliced_form        
            
    print(spliced_form)

prot_seq = Seq(spliced_form).transcribe().translate()
print(prot_seq)

with open('ID_SPLC\\SPLC_output.txt', 'w') as f:
        f.write(str(prot_seq))