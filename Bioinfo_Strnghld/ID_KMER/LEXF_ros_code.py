data = open('ID_LEXF\\rosalind_lexf.txt').read()
input = data.split('\n')
alphabet = input[0].split(' ')
n = int(input[1]) 

# print(alphabet,n)
k = 0
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


output = lexi_order(alphabet,n)

output = '\n'.join(output)
with open('LEXF_output.txt', 'w') as f:
        f.write(output)

