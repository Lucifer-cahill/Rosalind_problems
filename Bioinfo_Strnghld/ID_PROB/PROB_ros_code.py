import math
data = open('ID_PROB\\rosalind_prob.txt').read()
# data = open('sample.txt').read()

input = data.split('\n')
seq = input[0]
gc_cont = [float(x) for x in input[1].split(' ')]
seq_cont = {'GC': 0, 'AT': 0}
for i in seq:
    if i == 'G' or i == 'C':
        seq_cont['GC'] += 1
    if i == 'A' or i == 'T':
        seq_cont['AT'] += 1

print(seq_cont)

output_lst = []
for x in gc_cont:
    gc_prob = x/2
    at_prob = (1-x)/2

    print(gc_prob,at_prob)
    outlog = seq_cont['GC']*math.log(gc_prob,10)+seq_cont['AT']*math.log(at_prob,10)
    output_lst.append(outlog)

print(output_lst)


output = ' '.join([str(x) for x in output_lst])
with open('ID_PROB\\PROB_output.txt', 'w') as f:
        f.write(output)