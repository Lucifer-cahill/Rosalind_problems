# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1e.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30274_5.txt").read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\Ecoli_genome.txt").read()
data = open('sample.txt').read()
input = data.split('\n')
genome = input[0]
[k,l,t] = [int(x) for x in input[1].split(' ')]


def findclumps(gen,l,k,t):
    freq_words_dict = {}
    clumps = []
    for i in range(len(gen)-k):
        if gen[i:i+k] in freq_words_dict:
            freq_words_dict[gen[i:i+k]].append(i)
        else:
            freq_words_dict[gen[i:i+k]] = [i]
    for key in freq_words_dict:
        if len(freq_words_dict[key]) >= t:
            lst = freq_words_dict[key]
            for i in range(len(lst)-t+1):
                if lst[i+t-1]-lst[i] <= l-k:
                    clumps.append(key)
                    break
    return clumps

output = findclumps(genome,l,k,t)

print(len(output))



# output = ' '.join([str(x) for x in output])
# with open('Chapter_1\\TB1_Output_files\\BA1E_output.txt', 'w') as f:
#         f.write(output)
# with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30274_5_output.txt", 'w') as f:
#          f.write(output)