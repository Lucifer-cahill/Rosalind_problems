from BA1G_ros_code import hamm_dist
# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1h.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_6.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
pattern = input[0]
genome = input[1]
d = int(input[2])

def appr_occur(gen,patt,d):
    occurrences = []
    m = len(gen)
    n = len(patt)
    for i in range(m-n+1):
        if hamm_dist(gen[i:i+n],patt) <= d:
            occurrences.append(i)
    
    return occurrences

output_list = appr_occur(genome,pattern,d)

# print(output_list)
print(len(genome))
print(len(output_list))

output = ' '.join([str(x) for x in output_list])
# with open('Chapter_1\\TB1_Output_files\\BA1H_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_2\\dataset_30278_6_output.txt", 'w') as f:
         f.write(output)