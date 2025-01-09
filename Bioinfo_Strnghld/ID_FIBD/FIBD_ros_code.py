data = open('rosalind_fibd.txt')
for i in data.readlines():
    input = i.split(' ')
    n = int(input[0])
    k = int(input[1])

n = 10
k = 4

fib = [0]*(k+1)
fib[1] = 1
fib[2] = 1

for i in range(n-1):
    fib[0] = sum(fib[-k+1:])
    for j in range(len(fib)-1,0,-1):
        fib[j] = fib[j-1]


    print(fib)