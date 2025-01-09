# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3d.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30183_6.txt").read()
data = open('sample.txt').read()
input = data.split('\n')

k = int(input[0])
text = input[1]

def debruijn_text(string, k):
    debruijn_adj_lst = {}
    kmer_list = []
    for i in range(len(string)-k+1):
        kmer_list.append(string[i:i+k])
    for kmer in kmer_list:
        if kmer[:-1] in debruijn_adj_lst:
            debruijn_adj_lst[kmer[:-1]].append(kmer[1:])
        else:
            debruijn_adj_lst[kmer[:-1]] = [kmer[1:]]

    return debruijn_adj_lst

output = debruijn_text(text,k)

for key in output:
    if output[key]:
        print(f'{key} ->', ','.join(output[key]))

# with open('Chapter_3\\TB3_Output_files\\BA3D_output.txt', 'w') as f:
#     for key in output:
#         if output[key]:
#             f.write(f'{key} -> ')
#             f.write(','.join(output[key]))
#             f.write('\n')
        
        
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30183_6_output.txt", 'w') as f:
#     for key in output:
#         if output[key]:
#             f.write(f'{key} : ')
#             f.write(' '.join(output[key]))
#             f.write('\n')

    





