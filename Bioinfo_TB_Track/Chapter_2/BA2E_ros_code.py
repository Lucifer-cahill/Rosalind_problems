data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2e.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30306_9.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
[k,t] = [int(x) for x in input[0].split(' ')]
dna_coll = input[1:]

# print(dna_coll)
def most_prob_kmer(string, k, profile_matrix):
    max_kmer_prob = 0
    output_kmer = ''
    for i in range(len(string)-k+1):
        kmer_prob = 1
        kmer = string[i:i+k]
        for i in range(len(kmer)):
            kmer_prob = kmer_prob*profile_matrix[kmer[i]][i]
        if kmer_prob > max_kmer_prob:
            max_kmer_prob = kmer_prob
            output_kmer = kmer
    if not output_kmer:
        output_kmer = string[:k]

    return output_kmer

def form_profile(seq_lst):
    n = len(seq_lst) + 4
    profile_matrix = { nt: [] for nt in 'ACGT'}
    for i in range(len(seq_lst[0])):
        for nt in profile_matrix:
            profile_matrix[nt].append(1/n)
        for seq in seq_lst:
            profile_matrix[seq[i]][i] += 1/n
    
    score = 0
    for i in range(len(seq_lst[0])):
        temp_lst = [profile_matrix[x][i] for x in profile_matrix]
        temp_lst.remove(max(temp_lst))
        score += sum(temp_lst)*n 
      
    return score,profile_matrix

def greedy_motif_search(string_set,k,t):
    best_motifs = [string[:k] for string in string_set]
    best_score, best_prof_mat = form_profile(best_motifs)
    motif_lst = []
    for i in range(len(string_set[0])-k+1):
        motif_lst.append(string_set[0][i:i+k])
        for j in range(1,t):
            score, prof_mat = form_profile(motif_lst)
            motif_lst.append(most_prob_kmer(string_set[j],k,prof_mat))
        score, prof_mat = form_profile(motif_lst)
        if score < best_score:
            best_motifs = motif_lst
            best_score = score
        motif_lst = []
    
    return best_motifs

output_list = greedy_motif_search(dna_coll,k,t)   
        
print(output_list)

output = ' '.join([str(x) for x in output_list])
with open('Chapter_2\\TB2_Output_files\\BA2E_output.txt', 'w') as f:
        f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30306_9_output.txt", 'w') as f:
#          f.write(output)