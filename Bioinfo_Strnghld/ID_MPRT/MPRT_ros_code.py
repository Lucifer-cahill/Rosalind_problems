import requests as r

Prot_seq_dict = {}
data = open('rosalind_mprt (2).txt').read()
# print(data)
temp = ''

for i in data:
    if i != '\n':
        temp += i
    if i == '\n':
        Prot_seq_dict[temp] = ''
        temp = ''
Prot_seq_dict[temp] = ''
# print(Prot_seq_dict)
    
for i in Prot_seq_dict:
    cID= i[:6]
    if len(i) < 6:
        continue

    baseUrl="http://www.uniprot.org/uniprot/"
    currentUrl=baseUrl+cID+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)

    seq = ''.join(cData.split('\n')[1:])
    # print(seq)
    Prot_seq_dict[i] = seq

# print(Prot_seq_dict)

for i in Prot_seq_dict:
    prot_seq = Prot_seq_dict[i]
    motif_loc = ''
    flag = False
    for j in range(len(prot_seq)):
        if j < len(prot_seq)-3:
            if prot_seq[j] == 'N':
                if prot_seq[j+1] != 'P':
                    if prot_seq[j+2] == 'S' or prot_seq[j+2] == 'T':
                        if prot_seq[j+3] != 'P':
                            motif_loc += str(j+1) + ' '
                            # print(prot_seq[j:j+4])
                            flag = True
    if flag:
        print(i)
        # print(Prot_seq_dict[i],'\n')
        print(motif_loc)

