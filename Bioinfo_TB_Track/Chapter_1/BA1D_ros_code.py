# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1d.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30273_5.txt").read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\Vibrio_cholerae.txt").read()

# data = open('sample.txt').read()
input = data.split('\n')
pattern = 'CTTGATCAT'
genome = input[0]

def find_occur(gen,patt):
    index_lst = []
    for i in range(len(gen)):
        if gen[i:i+len(patt)] == patt:
            index_lst.append(i)
    
    return index_lst

output = find_occur(genome,pattern)

# print(output)

output = ' '.join([str(x) for x in output])
# with open('Chapter_1\\TB1_Output_files\\BA1D_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\Vibrio_cholerae_all_occur.txt", 'w') as f:
        f.write(output)