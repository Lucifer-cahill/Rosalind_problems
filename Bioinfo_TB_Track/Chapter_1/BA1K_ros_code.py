data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1k.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')

text = input[0]
k = int(input[1])

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

kmer_list = lexi_order(['A','C','G','T'],k)

def freq_array(txt,kmer_list):
    freq_dict = {nt : 0 for nt in kmer_list}
    for i in range(len(txt)-k+1):
        freq_dict[txt[i:i+k]] += 1
    return freq_dict

output_list = list(freq_array(text,kmer_list).values())

# print(output_list)

output = ' '.join([str(x) for x in output_list])
with open('Chapter_1\\TB1_Output_files\\BA1K_output.txt', 'w') as f:
        f.write(output)