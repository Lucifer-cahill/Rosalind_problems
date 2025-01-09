# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1c.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30273_2.txt").read()
# data = open('sample.txt').read()
input = data[:-1]

def rev_comp(string):
    comp_dict = {'A':'T','G':'C','T':'A','C':'G'}
    output = ''
    for i in string:
        output = comp_dict[i] + output
    return output

output = rev_comp(input)

print(output)
# output = ' '.join([str(x) for x in output_list])
# with open('Chapter_1\\TB1_Output_files\\BA1C_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30273_2_output.txt", 'w') as f:
         f.write(output)