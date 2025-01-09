import random
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\Dosr_upgenes.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

gene_upstream_coll = input.copy()

def consensus_finder(kmer_list):
    consensus_motif = ''
    profile_matrix = { nt: [] for nt in 'ACGT'}
    nt_num = {0: 'A',1: 'C', 2 : 'G', 3: 'T'}
    n = len(kmer_list[0])
    for i in range(len(kmer_list[0])):
        for nt in profile_matrix:
            profile_matrix[nt].append(0)
        for seq in kmer_list:
            profile_matrix[seq[i]][i] += 1
        nt_count = []
        for key in profile_matrix:
            nt_count.append(profile_matrix[key][i])
        con_nt = nt_count.index(max(nt_count))
        consensus_motif += nt_num[con_nt]

    return consensus_motif

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

# for k in [8,9,10,11,12]:
#     median_kmer = median_string(gene_upstream_coll,k)
#     print(median_kmer)

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
    return best_motifs,best_score

for k in [8,9,10,11,12]:
    best_output = []
    best_score = len(gene_upstream_coll)*k + 5 
    for j in range(1000):
        output_motifs, iter_score = randomized_motif_search(gene_upstream_coll, k, 10)
        if iter_score < best_score:
            best_output = output_motifs
            best_score = iter_score

    print(best_output,best_score)
    print(f'{k} consensus motif', consensus_finder(best_output))

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

for k in [8,9,10,11,12]:
    best_output = []
    best_score = len(gene_upstream_coll)*k + 5 
    for j in range(2000):
        output_motifs, iter_score = gibbs_sampler(gene_upstream_coll, k, 10, 200)
        if iter_score < best_score:
            best_output = output_motifs
            best_score = iter_score

    print(best_output,best_score)
    print(f'{k} consensus motif', consensus_finder(best_output))

# print(output_list)

# output = ' '.join([str(x) for x in output_list])

# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_4\\dataset_30272_13_output.txt", 'w') as f:
#          f.write(output)