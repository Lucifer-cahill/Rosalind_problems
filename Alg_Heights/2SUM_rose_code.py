# data = open('Input_files\\rosalind_2sum.txt').read()
data = open('sample.txt').read()
input = data.split('\n')
k,n = [int(x) for x in input[0].split(' ')]

for i in range(1,k+1):
    output = []
    arr = sorted([int(x) for x in input[i].split(' ')])
    start = 0
    end = len(arr) - 1
    sum2 = arr[start] + arr[end]
    print(arr)
    while start < n//2+1 and end >= n//2:
        sum2 = arr[start] + arr[end]
        print(sum2)
        if sum2 == 0:
            output.append([start,end])
            break
        if sum2 < 0:
            start += 1
        if sum2 > 0:
            end -= 1

    print(output)        

         



# print(output_list)

# output = ' '.join([str(x) for x in output_list])
# with open('Output_files\\mer_output.txt', 'w') as f:
#         f.write(output)
