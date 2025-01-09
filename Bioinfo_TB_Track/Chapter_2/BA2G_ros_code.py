import random
# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2g.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\dataset_30309_11.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
[k,t,n] = [int(x) for x in input[0].split(' ')]
dna_coll = input[1].split(' ')


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

def motif_choice(profile, string, k):
    output_motif = ''
    prob_dist = []
    for i in range(len(string)-k+1):
        kmer_prob = 1
        kmer = string[i:i+k]
        for i in range(len(kmer)):
            kmer_prob = kmer_prob*profile[kmer[i]][i]
        prob_dist.append(kmer_prob)
    sum_prob_dist = sum(prob_dist)
    for i in range(len(prob_dist)):
        prob_dist[i] = prob_dist[i] / sum_prob_dist
    
    [r_2] = random.choices([x for x in range(len(string)-k+1)], weights = prob_dist)
    output_motif = string[r_2:r_2+k]
    return output_motif

def gibbs_sampler(string_set,k,t,n):
    init_motifs = []
    for string in string_set:
        rnd_1 = random.randint(0,len(string)-k)
        init_motifs.append(string[rnd_1:rnd_1+k])
    best_motifs = init_motifs
    best_score, best_prof_mat = form_profile(best_motifs)
    for j in range(n):
        r_1 = random.randint(0,t-1)
        temp_motifs = init_motifs[:r_1] + init_motifs[r_1+1:]
        score,prof_mat = form_profile(temp_motifs)
        motif_i = motif_choice(prof_mat,string_set[r_1],k)
        new_motifs = init_motifs[:r_1] + [motif_i] + init_motifs[r_1+1:]
        score,prof_mat = form_profile(new_motifs)
        if score < best_score:
            best_motifs = new_motifs
            best_score = score
    
        init_motifs = new_motifs
    
    return best_motifs, best_score


best_output = []
best_score = len(dna_coll)*k + 5 
for j in range(20):
    output_motifs, iter_score = gibbs_sampler(dna_coll, k, t, n)
    if iter_score < best_score:
        best_output = output_motifs
        best_score = iter_score

print(best_output,best_score)

# print(output_list)

output = ' '.join([str(x) for x in best_output])
# with open('Chapter_2\\TB2_Output_files\\BA2G_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\dataset_30309_11_output.txt", 'w') as f:
         f.write(output)