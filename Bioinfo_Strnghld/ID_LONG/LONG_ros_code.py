import random
supstr = "".join(random.choice('AGCT') for _ in range(46))
print(supstr)

frag_lst = []

for i in range(10):
    frag_lst.append(supstr[4*i:4*i + 10])
print(frag_lst)
random.shuffle(frag_lst)
print(frag_lst)
# from Bio.Seq import Seq
# from Bio import SeqIO
# # data = open('ID_LONG\\rosalind_long.txt').read()
# data = open('sample.txt').read()
# seq_dict = {}
# for seq_data in SeqIO.parse('sample.txt','fasta'):
#     seq_dict[seq_data.id] = str(seq_data.seq)
# print(seq_dict)
# frag_lst = list(seq_dict.values())
# sup_str = 'ACATATTAGTACCGCCGAGC'
# print(sup_str)
# frag_lst = ['GTACC', 'ATTAG', 'TTAGT', 'TAGTA', 'TACCG', 'ACATA', 'AGTAC', 'ATATT', 'TATTA', 'CATAT'] 
# print(frag_lst)
super_str = ''
p = 0
flag = True
while frag_lst:
    flag = True
    # print('_______')
    # print(frag_lst)
    # print(super_str)
    n = len(frag_lst[0])
    fh = frag_lst[0][:n//2]
    sh = frag_lst[0][n//2:]
    # print(n,fh,sh)
    if super_str:
        if frag_lst[0] in super_str:
            frag_lst.pop(0)
            continue
        if fh in super_str:
            m = 0
            while fh in super_str:
                m += 1
                fh = frag_lst[0][:(n//2+m)]
            if super_str.endswith(frag_lst[0][:(n//2+m-1)]):
                super_str += frag_lst[0][(n//2+m-1):]
                flag = True 
                frag_lst.pop(0)
            else:
                flag = False
        if frag_lst:
            if sh in super_str:
                m = 0
                while sh in super_str:
                    m+=1
                    if m <= n//2:
                        sh = frag_lst[0][(n//2-m):]

                if super_str.startswith(frag_lst[0][(n//2-m+1):]):
                    super_str = frag_lst[0][:(n//2-m+1)] + super_str
                    flag = True
                    frag_lst.pop(0)
                else:
                    flag = False
            
        else:
            frag_lst.append(frag_lst[0])
            frag_lst.pop(0)

        if not flag:
            frag_lst.append(frag_lst[0])
            frag_lst.pop(0)

    else:
        super_str = super_str + frag_lst[0]
        frag_lst.pop(0)
    
    p+=1


    
print(super_str)


# output = ' '.join([str(x) for x in output])
# with open('LGIS_output.txt', 'w') as f:
#         f.write(output)
