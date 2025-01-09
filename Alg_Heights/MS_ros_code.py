data = open('Input_files\\rosalind_ms.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')

arr = [int(k) for k in input[1].split(' ')]

def merge(lst_a,lst_b):
    lst_c = []
    while lst_a and lst_b:
        if lst_a[0] < lst_b[0]:
            lst_c.append(lst_a[0])
            lst_a.pop(0)
        else:
            lst_c.append(lst_b[0])
            lst_b.pop(0)
    if lst_a:
        lst_c = lst_c + lst_a
    if lst_b:
        lst_c = lst_c + lst_b
    return lst_c        

def merge_sort(lst):
    n = len(lst)
    if len(lst) == 1:
        return lst
    else:
        return merge(merge_sort(lst[:n//2]),merge_sort(lst[n//2:]))
    
sort_arr = merge_sort(arr)

# print(sort_arr)




# print(output_list)

output = ' '.join([str(x) for x in sort_arr])
with open('Output_files\\ms_output.txt', 'w') as f:
        f.write(output)