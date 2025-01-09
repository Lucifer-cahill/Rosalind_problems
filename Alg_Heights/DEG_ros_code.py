data = open('Input_files\\rosalind_deg.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')
m,n = [int(k) for k in input[0].split(' ')]
output = [0 for j in range(m)]
for i in range(1,n+1):
    x,y = [int(k) for k in input[i].split(' ')]
    output[x-1] += 1
    output[y-1] += 1

# print(output)

output = ' '.join([str(x) for x in output])
with open('Output_files\\deg_output.txt', 'w') as f:
        f.write(output)

