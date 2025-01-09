# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1f.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\Salmonella_enterica.txt").read()
data = open('sample.txt').read()

genome = data[:-1]
def skew(string):
    skew_val = 0
    for i in string:
        if i == 'C':
            skew_val -= 1
        if i == 'G':
            skew_val += 1
    return skew_val

def min_skew(string):
    skew_val = 0
    min_skew = 0
    skew_lst = []
    for i in string:
        if i == 'C':
            skew_val -= 1
        if i == 'G':
            skew_val += 1
        skew_lst.append(skew_val)
        if skew_val < min_skew:
            min_skew = skew_val
    min_skew_lst = []
    for i in range(len(skew_lst)):
        if skew_lst[i] == min_skew:
            min_skew_lst.append(i+1)
    return min_skew_lst

output_list = min_skew(genome)
# print(len(genome))
print(output_list)

output = ' '.join([str(x) for x in output_list])
# with open('Chapter_1\\TB1_Output_files\\BA1F_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\Salmonella_enterica_skew.txt", 'w') as f:
         f.write(output)