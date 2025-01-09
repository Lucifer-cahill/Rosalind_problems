from Bio.Seq import Seq
from Bio import SeqIO
# data = open('ID_LONG\\rosalind_long.txt').read()
# data = open('sample.txt').read()
seq_lst = []
for seq_data in SeqIO.parse('sample.txt','fasta'):
    seq_lst.append(str(seq_data.seq))

short_seq = min(seq_lst)
nt_lst = set(short_seq)
seq_lst.remove(short_seq)
motif_dict = { nt: [[] for i in range(len(seq_lst))] for nt in nt_lst}

print(motif_dict)
for seq in range(len(seq_lst)):
    for j in range(len(seq_lst[seq])):
        if seq_lst[seq][j] in motif_dict:
            motif_dict[seq_lst[seq][j:j+1]][seq].append(j)

print(motif_dict)
def expand(seq_lst, dict_1, nt):
    print('_______________')
    dict_1_new = {}
    flag = False
    for key in dict_1:
        flag = False
        for lst in dict_1[key]:
            if len(lst) > 0:
                flag = True
            else:
                flag = False
                break
        if flag:
            for k in nt:
                dict_1_new[key + k] = [[] for i in range(len(seq_lst))]
    for key in dict_1:
        for i in range(len(dict_1[key])):
            for l in dict_1[key][i]:
                if seq_lst[i][l:l+len(list(dict_1_new.keys())[0])] in dict_1_new:
                    # print(seq_lst[i][l:l+2])
                    dict_1_new[seq_lst[i][l:l+len(list(dict_1_new.keys())[0])]][i].append(l)
            
    return dict_1_new

new_dict = expand(seq_lst,motif_dict,nt_lst)

print(new_dict)

new_new_dict = expand(seq_lst,new_dict,nt_lst)

print(new_new_dict)

trip_new_dict = expand(seq_lst,new_new_dict,nt_lst)

print(trip_new_dict)

        

    




# output = ' '.join([str(x) for x in output])
# with open('LGIS_output.txt', 'w') as f:
#         f.write(output)








