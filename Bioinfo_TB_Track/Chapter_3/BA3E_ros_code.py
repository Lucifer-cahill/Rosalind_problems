# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3e.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30184_8.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

kmers = input[0].split(' ')

def debruijn_kmers(kmer_list):
    debruijn_adj_lst = {}
    for kmer in kmer_list:
        if kmer[:-1] in debruijn_adj_lst:
            debruijn_adj_lst[kmer[:-1]].append(kmer[1:])
        else:
            debruijn_adj_lst[kmer[:-1]] = [kmer[1:]]

    return debruijn_adj_lst

output = debruijn_kmers(kmers)

for key in output:
    if output[key]:
        print(f'{key} ->', ','.join(output[key]))

# with open('Chapter_3\\TB3_Output_files\\BA3E_output.txt', 'w') as f:
#     for key in output:
#         if output[key]:
#             f.write(f'{key} -> ')
#             f.write(','.join(output[key]))
#             f.write('\n')
        
        
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30184_8_output.txt", 'w') as f:
    for key in output:
        if output[key]:
            f.write(f'{key} : ')
            f.write(' '.join(output[key]))
            f.write('\n')

    





