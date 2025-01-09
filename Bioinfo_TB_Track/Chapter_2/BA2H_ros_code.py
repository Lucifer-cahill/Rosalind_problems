# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2h.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30312_1.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
pattern = input[0]
dna_coll = input[1].split(' ')

def hamm_dist(str_1,str_2):
    return sum([int(str_1[i] != str_2[i]) for i in range(len(str_1))])

def min_dist_motif(pattern,string):
    k = len(pattern)
    min_dist = k + 1
    for i in range(len(string)-k):
        d = hamm_dist(pattern,string[i:i+k])
        if  d < min_dist:
            min_dist = d
            motif = string[i:i+k]
    
    return min_dist

def hamm_dist_coll(patt, string_set):
    dist_coll = 0
    for string in dna_coll:
        min_dist = min_dist_motif(pattern,string)
        dist_coll += min_dist
    
    return dist_coll

output = hamm_dist_coll(pattern,dna_coll)


print(output)

# with open('Chapter_2\\TB2_Output_files\\BA2H_output.txt', 'w') as f:
#         f.write(str(output))
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30312_1_output.txt", 'w') as f:
         f.write(str(output))