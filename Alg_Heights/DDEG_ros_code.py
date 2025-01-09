data = open('Input_files\\rosalind_ddeg.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')
m,n = [int(k) for k in input[0].split(' ')]
neighbor_dict = {j+1 : [] for j in range(m)}
deg_arr = [0 for j in range(m)]
print(neighbor_dict)
for i in range(1,n+1):
    x,y = [int(k) for k in input[i].split(' ')]
    neighbor_dict[x].append(y)
    neighbor_dict[y].append(x)

output = [0 for j in range(m)]
for i in neighbor_dict:
    output[i-1] = sum([len(neighbor_dict[j]) for j in neighbor_dict[i]])

print(output)


output = ' '.join([str(x) for x in output])
with open('Output_files\\DDEG_output.txt', 'w') as f:
        f.write(output)