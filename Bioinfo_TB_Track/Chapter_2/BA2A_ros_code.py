from itertools import combinations
# data = open('Chapter_2\\TB2_Input_files\\rosalind_ba2a.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30302_8_v2.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

[k,d] = [int(x) for x in input[0].split(' ')]
dna_coll = input[1].split(' ')
nt_lst = list('ACGT')

print(dna_coll)

def lexi_order(alphabet,n):
    lexi_lst_old = ['']
    lexi_lst_new = []
    for i in range(n):
        for k in lexi_lst_old:
            for i in range(len(alphabet)):
                lexi_lst_new.append(k+alphabet[i])
        lexi_lst_old = lexi_lst_new
        lexi_lst_new = []
    
    return lexi_lst_old

def approx_matches(string,nt_lst,d):
    k = len(string)
    neighborhood = []
    comb_lst = list(combinations(range(k),d))
    nt_lst = lexi_order(nt_lst,d)
    temp = string
    for tuple in comb_lst:
        for tup in nt_lst:
            temp = string
            for i in range(len(tuple)):
                temp = temp[:tuple[i]] + tup[i] + string[tuple[i]+1:]
            if temp in neighborhood:
                continue       
            else:
                neighborhood.append(temp)
    return neighborhood

def motif_finder(seqs,k,d):
    old_comm_lst = [] 
    new_comm_lst = []
    for seq in seqs:
        temp_lst = []
        for i in range(len(seq)-k+1):
            temp_lst += approx_matches(seq[i:i+k],nt_lst,d)
        
        for motif in set(temp_lst):
            if motif in old_comm_lst or not old_comm_lst:
                new_comm_lst.append(motif)
        # print(new_comm_lst)
        old_comm_lst = new_comm_lst
        new_comm_lst = []

    return old_comm_lst

output_list = motif_finder(dna_coll,k,d)

print(output_list)

output = ' '.join([str(x) for x in output_list])
# with open('Chapter_2\\TB2_Output_files\\BA2A_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_3\\dataset_30302_8_v2_output.txt", 'w') as f:
         f.write(output)