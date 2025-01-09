data = open('Input_files\\rosalind_fibo.txt').read()
# data = open('sample.txt').read()

n = int(data)


fibn = 1 # F_n
fibn1 = 1 # F_{n-1}
for dummy in range(2,n):
    fib = fibn + fibn1
    fibn1 = fibn
    fibn = fib

output = fib

print(output)

# output = ' '.join([str(x) for x in output])
# with open('Output_files\\FIBO_output.txt', 'w') as f:
#         f.write(output)

