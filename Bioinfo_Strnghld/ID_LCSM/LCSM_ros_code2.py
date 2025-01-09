# data = open('ID_LCSM\\rosalind_lcsm.txt').read()
# data = open('sample.txt').read()
from Bio.Seq import Seq
from Bio import SeqIO
seq_lst = []
for seq_data in SeqIO.parse('ID_LCSM\\rosalind_lcsm.txt','fasta'):
    seq_lst.append(str(seq_data.seq))

short_seq = min(seq_lst)
nt_lst = set(short_seq)
motif_dict = { nt: [[] for i in range(len(seq_lst))] for nt in nt_lst}

def search_nt(seq_lst,motif_dict):
    for i in range(len(seq_lst)):
        for j in range(len(seq_lst[i])):
            if seq_lst[i][j] in motif_dict:
                motif_dict[seq_lst[i][j]][i].append(j)
    
    return motif_dict

def find_shared_motif(old_dict):
    com_lst = []
    flag = False
    for key in old_dict:
        flag = False
        for lst in old_dict[key]:
            if len(lst) > 0:
                flag = True
            else:
                flag = False
                break
        if flag:
            com_lst.append(key)
            
    return com_lst

def expand(common_lst,nt_lst):
    new_dict = {}
    for string in common_lst:
        for nt in nt_lst:
            new_dict[string+nt] = [[] for i in range(len(seq_lst))] 
    
    return new_dict

def search_motif(seq_lst,old_dict,new_dict):
    motif_len = len(list(new_dict.keys())[0])
    for motif in old_dict:
        for i in range(len(seq_lst)):
            for l in old_dict[motif][i]:
                if seq_lst[i][l:l+motif_len] in new_dict:
                    new_dict[seq_lst[i][l:l+motif_len]][i].append(l)

    return new_dict


motif_dict = search_nt(seq_lst,motif_dict)
shared_motif_lst = find_shared_motif(motif_dict)
new_motif_dict = expand(shared_motif_lst,nt_lst)

while len(new_motif_dict) > 0:
    new_motif_dict = search_motif(seq_lst,motif_dict,new_motif_dict)
    motif_dict = new_motif_dict.copy()
    # print(motif_dict)
    print(len(motif_dict))

    temp = find_shared_motif(motif_dict)
    if temp:
        shared_motif_lst = temp.copy()
    else:
        break
    new_motif_dict = expand(shared_motif_lst,nt_lst) 

print(shared_motif_lst)


# output = ' '.join([str(x) for x in output])
with open('ID_LCSM\\LCSM_Text.txt', 'w') as f:
        f.write(shared_motif_lst[0])