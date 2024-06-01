data = open('rosalind_fib.txt')
for i in data.readlines():
    input = i.split(' ')
    n = int(input[0])
    k = int(input[1])

fib_1 = 1
fib_2 = 0
fib_n = 0

for i in range(n-1):
    fib_n = fib_1 + k*fib_2
    fib_2 = fib_1 
    fib_1 = fib_n 

print(fib_n)