data = open('Chapter_1\\TB1_Input_files\\rosalind_ba1l.txt').read()
# data = open('sample.txt').read()

input = data[:-1]

def patt2num(txt):
    nt_to_num_dict = {'A': 0,
                  'C': 1,
                  'G': 2,
                  'T': 3}
    output = 0
    for i in range(len(txt)-1,-1,-1):
        output += (4**(len(txt)-1-i))*nt_to_num_dict[txt[i]]

    return output

print(patt2num(input))

