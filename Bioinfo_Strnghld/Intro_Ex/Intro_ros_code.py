# data = open('sample.txt').read()


# data = open('Intro_Ex\\rosalind_ini2.txt').read()
# input = data.split(' ')
# output = int(input[0])**2 + int(input[1])**2
# print(output)


# data = open('Intro_Ex\\rosalind_ini3.txt').read()
# data_txt = data.split('\n')[0]
# data_int = data.split('\n')[1]
# slices = data_int.split(' ')
# slices = [int(x) for x in slices]
# print(data_txt[slices[0]:(slices[1]+1)],data_txt[slices[2]:(slices[3]+1)])


# data = open('Intro_Ex\\rosalind_ini4.txt').read()
# input = data.split(' ')
# sum = []
# for i in input:
#     i = int(i)
#     if i%2 == 0:
#         sum.append(((i)/2)**2)
#     else:
#         sum.append(((i+1)/2)**2)
# print(sum[1] - sum[0])


data = open('Intro_Ex\\rosalind_ini5.txt').read()
input = data.split('\n')
with open('ini5_output.txt', 'w') as f:
    for i in range(0,len(input),2):
        f.write(input[i] + '\n')


# data =  open('Intro_Ex\\rosalind_ini6.txt').read()
# input = data.split(' ')
# output_dict = {}

# for i in input:
#     if i in output_dict:
#         output_dict[i] += 1
#     else:
#         output_dict[i] = 1
# print(output_dict)
# with open('ini6_output.txt', 'w') as f:
#     for key, value in output_dict.items():
#         f.write(f'{key} {value}' + '\n')


