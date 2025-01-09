data = open('Chapter_3\\TB3_Input_files\\rosalind_ba3a.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30153_3.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
k = int(input[0])
text = input[1]

def kmer_composition(string,k):
    comp = []
    for i in range(len(string)-k+1):
        comp.append(string[i:i+k])
    
    return comp

output_list = kmer_composition(text,k)

print(output_list)

output = ' '.join([str(x) for x in output_list])
with open('Chapter_3\\TB3_Output_files\\BA3A_output.txt', 'w') as f:
        f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_2\\2_Week_1\\dataset_30153_3_output.txt", 'w') as f:
#          f.write(output)