from itertools import combinations
data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1i.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_9.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
text = input[0]
[k,d] = [int(x) for x in input[1].split(' ')]
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

def hamm_dist(dna_s,dna_t):
    count = 0
    for i in range(len(dna_s)):
        if dna_s[i] != dna_t[i]:
            count += 1
    return count

def approx_matches(string,nt_lst,d):
    k = len(string)
    output_list = []
    comb_lst = list(combinations(range(k),d))
    nt_lst = lexi_order(nt_lst,d)
    temp = string
    for tuple in comb_lst:
        for tup in nt_lst:
            temp = string
            for i in range(len(tuple)):
                temp = temp[:tuple[i]] + tup[i] + string[tuple[i]+1:]
            if temp in output_list:
                continue       
            else:
                output_list.append(temp)
    return output_list

def freq_appr_words(txt,k,d,nt_lst):
    freq_words_dict = {}
    for i in range(len(txt)-k+1):
        appr_matches = approx_matches(txt[i:i+k],nt_lst,d)
        for j in range(len(appr_matches)):
            if appr_matches[j] not in freq_words_dict:
                freq_words_dict[appr_matches[j]] = 1
            else:
                freq_words_dict[appr_matches[j]] += 1
    
    max_val = max(list(freq_words_dict.values()))
    freq_words = []
    for key in freq_words_dict:
        if freq_words_dict[key] == max_val:
            freq_words.append(key)

    return freq_words


output_list = freq_appr_words(text,k,d,nt_lst)

print(output_list)

output = ' '.join([str(x) for x in output_list])
with open('Chapter_1\\TB1_Output_files\\BA1I_output.txt', 'w') as f:
        f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_9_output.txt", 'w') as f:
#          f.write(output)