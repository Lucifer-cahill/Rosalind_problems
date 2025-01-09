# import random
# supstr = "".join(random.choice('AGCT') for _ in range(46))
# print(supstr)
# frag_lst = []
# for i in range(10):
#     frag_lst.append(supstr[4*i:4*i + 10])
# print(frag_lst)
# random.shuffle(frag_lst)
# print(frag_lst)
from Bio.Seq import Seq
from Bio import SeqIO
# data = open('ID_LONG\\rosalind_long.txt').read()
# data = open('sample.txt').read()
seq_dict = {}
for seq_data in SeqIO.parse('ID_LONG\\rosalind_long.txt','fasta'):
    seq_dict[seq_data.id] = str(seq_data.seq)
print(seq_dict)
frag_lst = list(seq_dict.values())
super_str = frag_lst[0]
frag_lst.pop(0)
p = 0
flag = False
while frag_lst:
    # print(super_str)
    flag = False
    temp = frag_lst[0]
    n = len(frag_lst[0])
    half = n//2
    fh = temp[:half]
    sh = temp[half:]
    # print(n,fh,sh)
    if temp in super_str:
        flag = True
    if fh in super_str:
        m = 1
        while fh in super_str:
            fh = temp[:(half+m)]
            m += 1
        fh = temp[:(half+m-2)]
        if super_str.endswith(fh):
            super_str = super_str + temp[(half+m-2):]
            flag = True

    if sh in super_str and not flag:
        m = 1
        while sh in super_str:
            sh = temp[(half-m):]
            m += 1
        sh = temp[(half-m+2):]
        if super_str.startswith(sh):
            super_str = temp[:(half-m+2)] + super_str  
            flag = True
    
    if flag:
        frag_lst.pop(0)
    else:
        frag_lst.append(temp)
        frag_lst.pop(0)

    p+=1

print(super_str)
        
# output = ' '.join([str(x) for x in output])
with open('ID_LONG\\LONG_output.txt', 'w') as f:
        f.write(super_str)
