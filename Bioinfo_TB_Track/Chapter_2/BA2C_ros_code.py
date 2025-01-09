import math
# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2c.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30305_3.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
text = input[0]
k = int(input[1])
prof_mat = {}
prof_mat['A'] = [float(x) for x in input[2].split(' ')]
prof_mat['C'] = [float(x) for x in input[3].split(' ')]
prof_mat['G'] = [float(x) for x in input[4].split(' ')]
prof_mat['T'] = [float(x) for x in input[5].split(' ')]

def most_prob_kmer(string, k, profile_matrix):
    max_kmer_prob = 0
    output_kmer = ''
    for i in range(len(string)-k):
        kmer_prob = 1
        kmer = string[i:i+k]
        for i in range(len(kmer)):
            kmer_prob = kmer_prob*profile_matrix[kmer[i]][i]
        if kmer_prob > max_kmer_prob:
            max_kmer_prob = kmer_prob
            output_kmer = kmer

    return output_kmer

output = most_prob_kmer(text,k,prof_mat)

print(output)

# with open('Chapter_2\\TB2_Output_files\\BA2C_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30305_3_output.txt", 'w') as f:
         f.write(output)