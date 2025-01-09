# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1g.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_3.txt").read()
data = open('sample.txt').read()

input = data.split('\n')
str_1 = input[0]
str_2 = input[1]

def hamm_dist(dna_s,dna_t):
    count = 0
    for i in range(len(dna_s)):
        if dna_s[i] != dna_t[i]:
            count += 1
    return count

print(hamm_dist(str_1,str_2))

# print(output_list)

# output = ' '.join([str(x) for x in output_list])
# with open('Chapter_1\\TB1_Output_files\\BA1C_output.txt', 'w') as f:
#         f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_3_output.txt", 'w') as f:
#          f.write(output)