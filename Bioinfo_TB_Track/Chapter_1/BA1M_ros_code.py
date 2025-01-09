data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1m.txt').read()
# data = open("D:\\IIT Madras\\Course material\\Bioinfo_coursera\\Bioinformatics_1\\1_Week_1\\dataset_30272_6.txt").read()
# data = open('sample.txt').read()
input = data.split('\n')
num = int(input[0])
k = int(input[1])

def num2patt(number,k):
    num_to_nt_dict = {0 : 'A',
                      1 : 'C',
                      2 : 'G',
                      3 : 'T'}
    pattern = ''
    while number > 4:
        pattern = num_to_nt_dict[number%4] + pattern
        number = number//4
    pattern = num_to_nt_dict[number] + pattern
    while len(pattern) < k:
        pattern = num_to_nt_dict[0] + pattern
    return pattern

print(num2patt(num,k))

    
