from math import comb
data = open('rosalind_lia (2).txt')
for i in data.readlines():
    input = i.split(' ')
    k = int(input[0])
    N = int(input[1])

print(k ,N)
  
p_tot = 0
for i in range(N):
    x = comb(2**k,i)*(1/4)**(i) * (3/4)**(2**k - i)
    # print(x)
    p_tot += x 
    # print(p_tot)

p_out = 1 - p_tot
print(p_out)
