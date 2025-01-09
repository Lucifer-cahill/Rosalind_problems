import random
# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2f.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\dataset_30307_5 (1).txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

[k,t] = [int(x) for x in input[0].split(' ')]
dna_coll = input[1].split(" ")

def form_profile(kmer_list):
    profile_matrix = { nt: [] for nt in 'ACGT'}
    n = len(kmer_list[0]) + 4
    for i in range(len(kmer_list[0])):
        for nt in profile_matrix:
            profile_matrix[nt].append(1/n)
        for seq in kmer_list:
            profile_matrix[seq[i]][i] += 1/n
    
    score = 0
    for i in range(len(kmer_list[0])):
        temp_lst = [profile_matrix[x][i] for x in profile_matrix]
        temp_lst.remove(max(temp_lst))
        score += sum(temp_lst)*n 
    
    return score,profile_matrix

def motif_finder(profile, string_set, k):
    output_motifs = []
    for string in string_set:
        max_kmer_prob = 0
        most_prob_kmer = ''
        for i in range(len(string)-k+1):
            kmer_prob = 1
            kmer = string[i:i+k]
            for i in range(len(kmer)):
                kmer_prob = kmer_prob*profile[kmer[i]][i]
            if kmer_prob > max_kmer_prob:
                max_kmer_prob = kmer_prob
                most_prob_kmer = kmer
        output_motifs.append(most_prob_kmer)

    return output_motifs


def randomized_motif_search(string_set,k,t):
    init_motifs = []
    for string in string_set:
        rnd_1 = random.randint(0,len(string)-k)
        init_motifs.append(string[rnd_1:rnd_1+k])
    
    best_motifs = init_motifs
    best_score, best_prof_mat = form_profile(best_motifs)
    score = len(string_set)*k + 20
    score,prof_mat = form_profile(init_motifs)
    
    while True:
        new_motifs = motif_finder(prof_mat,string_set,k)
        score,prof_mat = form_profile(new_motifs)
        if score < best_score:
            best_motifs = new_motifs
            best_score = score
            
        else:
            break
    # print(best_motifs,best_score)
    return best_motifs,best_score

best_output = []
best_score = len(dna_coll)*k + 5 
for j in range(1000):
    output_motifs, iter_score = randomized_motif_search(dna_coll, k, t)
    if iter_score < best_score:
        best_output = output_motifs
        best_score = iter_score

print(best_output,best_score)

output = ' '.join([str(x) for x in best_output])
# with open('Chapter_2\\TB2_Output_files\\BA2F_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\dataset_30307_5_output.txt", 'w') as f:
         f.write(output)