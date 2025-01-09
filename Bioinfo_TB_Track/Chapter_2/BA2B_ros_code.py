import math
# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2b.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30304_9.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
k = int(input[0])

dna_coll = input[1:-1]

print(dna_coll) 

def hamm_dist(str_1,str_2):
    return sum([int(str_1[i] != str_2[i]) for i in range(len(str_1))])


def all_possible_kmers(k):
    nt_lst = list('ACGT')
    patterns_lst = ['']
    patterns_lst_new = []
    for i in range(k):
        for ele in patterns_lst:
            patterns_lst_new += [ele + nt for nt in nt_lst]
        patterns_lst = patterns_lst_new
        patterns_lst_new = []

    return patterns_lst

def min_dist_motif(pattern,string):
    k = len(pattern)
    min_dist = k + 1
    for i in range(len(string)-k):
        d = hamm_dist(pattern,string[i:i+k])
        if  d < min_dist:
            min_dist = d
            motif = string[i:i+k]
    
    return min_dist

def median_string(string_set,k):
    patterns_lst = all_possible_kmers(k)
    min_dist_coll = k*len(string_set[0])+1
    for pattern in patterns_lst:
        dist_coll = 0
        for string in string_set:
            min_dist = min_dist_motif(pattern,string)
            dist_coll += min_dist
        if dist_coll < min_dist_coll:
            min_dist_coll = dist_coll
            output_string = pattern
    
    return output_string
    

output = median_string(dna_coll,k)

print(output)

# with open('Chapter_2\\TB2_Output_files\\BA2B_output.txt', 'w') as f:
#         f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30304_9_output.txt", 'w') as f:
#          f.write(output)