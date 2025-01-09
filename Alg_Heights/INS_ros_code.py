data = open('Input_files\\rosalind_ins.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')

lst = [int(x) for x in input[1].split(' ')]
print(lst)
count = 0
for i in range(1,len(lst)):
    for j in range(i, 0,-1):
        if  lst[j] < lst[j-1]:
            lst[j-1],lst[j] = lst[j],lst[j-1]
            count += 1
print('Sorted List :',lst, count, 'swaps')


# print(output_list)

# output = ' '.join([str(x) for x in output_list])
# with open('Output_files\\bins_output.txt', 'w') as f:
#         f.write(output)

