data = open('ID_RSTR\\rosalind_rstr.txt').read()
# data = open('sample.txt').read()
input = data.split('\n')
n,gc_cont = [float(x) for x in input[0].split(' ')]
seq = input[1]
gc_count = 0
at_count = 0
for i in seq:
    if i == 'G' or i == 'C':
        gc_count +=1
    if i == 'A' or i == 'T':
        at_count +=1

prob = 1-(1-((gc_cont/2)**gc_count*((1-gc_cont)/2)**at_count))**n

print(round(prob,3))
    

# output = ' '.join([str(x) for x in output])
# with open('LGIS_output.txt', 'w') as f:
#         f.write(output)