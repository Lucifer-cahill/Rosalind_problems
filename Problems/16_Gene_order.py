import math 


n = 7
fact = math.factorial(n)
lst = [x+1 for x in range(n)]
def permutations(lst):
    # print('call',lst)
    n = len(lst)
    if n == 0:
        return 
    if n == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        rem_lst = lst[:i] + lst[i+1:]
        # print(rem_lst)
        for p in permutations(rem_lst):
            l.append([lst[i]] + p) 
    return l
        

out = permutations(lst)
total = str(fact) + '\n'
for i in out:
    temp = ''
    for j in i:
        temp += str(j) + ' '
    total += temp + '\n'

with open('GeneOrder_output.txt', 'w') as f:
    f.write(total)
