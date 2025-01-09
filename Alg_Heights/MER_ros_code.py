data = open('Input_files\\rosalind_mer.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')
arr_A = [int(k) for k in input[1].split(' ')]
arr_B = [int(k) for k in input[3].split(' ')]

arr_C = []
while arr_A and arr_B:
    if arr_A[0] >= arr_B[0]:
        arr_C.append(arr_B[0])
        arr_B.pop(0)
    else:
        arr_C.append(arr_A[0])
        arr_A.pop(0)
while arr_A:
    arr_C.append(arr_A[0])
    arr_A.pop(0)
while arr_B:
    arr_C.append(arr_B[0])
    arr_B.pop(0)

print(arr_C)

output = ' '.join([str(x) for x in arr_C])
with open('Output_files\\MER_output.txt', 'w') as f:
        f.write(output)