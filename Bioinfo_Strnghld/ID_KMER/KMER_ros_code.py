data = open('ID_KMER\\rosalind_kmer.txt').read()
# data = open('sample.txt').read()
seq = ''.join(data.split('\n')[1:])

from LEXF_ros_code import lexi_order

lexi_lst = lexi_order([x for x in 'ACGT'],4)

kmer_dict = {kmer : 0 for kmer in lexi_lst}
# print(kmer_dict)

for i in range(len(seq)-3):
    kmer_dict[seq[i:i+4]] += 1

output = ' '.join([str(x) for x in kmer_dict.values()]) 

# output = ' '.join([str(x) for x in output])
with open('ID_KMER\\KMER_output.txt', 'w') as f:
        f.write(output)