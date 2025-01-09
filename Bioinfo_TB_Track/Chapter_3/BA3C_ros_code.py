data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3c.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30182_10.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
kmer_coll = input[0].split(' ')


def overlap_adj_list(kmers):
    adj_lst = {kmer : [] for kmer in kmers}
    for key in adj_lst:
        for kmer in kmers:
            flag = True
            for i in range(len(key)-1):
                if key[i+1] != kmer[i]:
                    flag = False
                    break
            if flag:
                adj_lst[key].append(kmer)
    return adj_lst

output = overlap_adj_list(kmer_coll)

for key in output:
    if output[key]:
        print(f'{key} ->', ' '.join(output[key]))

# with open('Chapter_3\\TB3_Output_files\\BA3C_output.txt', 'w') as f:
#     for key in output:
#         if output[key]:
#             f.write(f'{key} -> ')
#             f.write(' '.join(output[key]))
#             f.write('\n')
        
        
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30182_10_output.txt", 'w') as f:
    for key in output:
        if output[key]:
            f.write(f'{key} : ')
            f.write(' '.join(output[key]))
            f.write('\n')