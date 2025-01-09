# data = open('ID_LEXF\\rosalind_lexf.txt').read()
data = open('sample.txt').read()
input = data.split('\n')
alphabet = input[0].split(' ')
n = int(input[1]) 

alphabet = alphabet
# print(alphabet,n)

# def lexv_list(ele,alphabet,n):
    
#     # lexi_lst_old = []
#     # for i in range(1,len(alphabet)):
#     #     k = 0
#     #     print('F',i,alphabet[i])
#     #     lexi_lst_old.append(alphabet[i])
#     #     while k < n:
#     #         k += 1
#     #         for j in range(len(alphabet)):
#     #             print('S',i,k,j,alphabet[i]+alphabet[k]+alphabet[j])
#     #             lexi_lst_old.append(alphabet[i]+alphabet[k]+alphabet[j])
#     if n == 1:

#         return 
#     else:

# def fact(n):
#     if n == 0 or n == 1: 
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))

def lexv_list(lexi_list,alphabet,n):
    temp = lexi_list.copy()
    if n == 1:
        alphabet = [''] + alphabet
        for k in lexi_list:
            for i in range(len(alphabet)):
                if len(k+alphabet[i])>0:
                    temp.append(k+alphabet[i])
        return temp
    else:
        for k in lexi_list:
            for j in range(len(alphabet)):
                temp.append(k+alphabet[j])
        temp = lexv_list(temp,alphabet,n-1)
        return temp

            














output = lexv_list([''],alphabet,n)
print(output)
# output = '\n'.join(output)
# with open('LEXF_output.txt', 'w') as f:
#         f.write(output)

