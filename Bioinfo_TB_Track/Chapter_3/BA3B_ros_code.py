# data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3b.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30182_3.txt").read()
# data = open('sample.txt').read()
input = data.split(' ')

def genome_path(string_set):
    output = string_set[0]
    for string in string_set[1:]:
        output += string[-1]
    
    return output

output = genome_path(input)
print(input)
print(output)

# output = ' '.join([str(x) for x in output_list])
# with open('Chapter_3\\TB3_Output_files\\BA3B_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30182_3_output.txt", 'w') as f:
         f.write(output)