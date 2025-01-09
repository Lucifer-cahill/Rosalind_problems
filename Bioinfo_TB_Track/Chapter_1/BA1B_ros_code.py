# data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1b.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30272_13.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
text = input[0]
k = int(input[1])

def freq_words(txt,k):
    freq_words_dict = {}
    for i in range(len(txt)-k):
        if txt[i:i+k] in freq_words_dict:
            freq_words_dict[txt[i:i+k]] += 1
        else:
            freq_words_dict[txt[i:i+k]] = 1
    max_freq = max(list(freq_words_dict.values()))
    most_freq_patt = []
    for key in freq_words_dict:
        if freq_words_dict[key] == max_freq:
            most_freq_patt.append(key)
    return most_freq_patt
    
most_freq_words = freq_words(text,k)

output = ' '.join([str(x) for x in most_freq_words])

# with open('Chapter_1\\TB1_Output_files\\BA1B_output.txt', 'w') as f:
#         f.write(output)
with open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30272_13_output.txt", 'w') as f:
         f.write(output)