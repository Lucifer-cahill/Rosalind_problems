data = open('Input_files\\rosalind_maj.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')
m,n = [int(k) for k in input[0].split(' ')]
half = n//2
freq_dict ={}
output = []
for i in range(m):
    flag = False
    arr = input[i+1].split(' ')
    for j in range(n):
        if arr[j] in freq_dict:
            freq_dict[arr[j]] += 1
        else:
            freq_dict[arr[j]] = 1
        if freq_dict[arr[j]] > half:
            output.append(int(arr[j]))
            flag = True
            break
    if not flag:
        output.append(-1)
    freq_dict = {}

print(output)
    
output = ' '.join([str(x) for x in output])
with open('Output_files\\maj_output.txt', 'w') as f:
        f.write(output)