data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1a.txt').read()
data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30272_6.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')

text = input[0]
pattern = input[1]
print(text)
print(pattern)

def pattcount(txt,patt):
    count = 0
    k = len(patt)
    for i in range(len(txt)-k):
        if txt[i:i+k] == patt:
            count += 1
    return count

print(pattcount(text,pattern))


# print(output_list)

# output = ' '.join([str(x) for x in output_list])
# with open('TB1_Output_files\\mer_output.txt', 'w') as f:
#         f.write(output)
