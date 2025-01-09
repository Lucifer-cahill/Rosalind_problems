data = open('Input_files\\rosalind_bins.txt').read()
# data = open('sample.txt').read()

input = data.split('\n')
sorted_lst = [int(x) for x in input[2].split(' ')]
search_items = [int(x) for x in input[3].split(' ')]

print(sorted_lst)

def binSearch(lst,n):
    l = 0
    u = len(lst) - 1
    m = 0
    while l <= u:
        m = (l+u)//2
        if lst[m] > n:
            u = m-1
        elif lst[m] < n:
            l = m+1
        else:
            return m+1
    return -1
output_list = []
for i in search_items:
     output_list.append(str(binSearch(sorted_lst,i)))

# print(output_list)

output = ' '.join([str(x) for x in output_list])
with open('Output_files\\bins_output.txt', 'w') as f:
        f.write(output)