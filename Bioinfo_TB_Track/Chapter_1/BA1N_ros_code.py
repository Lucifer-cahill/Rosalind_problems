from itertools import combinations
# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1n.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30282_4.txt").read()
# data = open('sample.txt').read()
# input = data.split('\n')
text = 'ACGT' #input[0]
d = 3 #int(input[1])
nt_lst = ['A','T','G','C']

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

output_list = approx_matches(text,nt_lst,d)

print(output_list)
print(len(output_list))
# output = '\n'.join([str(x) for x in output_list])
# with open('Chapter_1\\TB1_Output_files\\BA1N_output.txt', 'w') as f:
#         f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30282_4_output.txt", 'w') as f:
#          f.write(output)