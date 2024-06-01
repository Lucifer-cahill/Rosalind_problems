from math import comb
data = open('rosalind_iprb.txt')
for i in data.readlines():
    input = i.split(' ')
    hod = int(input[0])
    het = int(input[1])
    hor = int(input[2])

tot_pop = hod + het + hor
prob_dom = (comb(hod,2) + hod*(het + hor) + 0.75*comb(het,2) + 0.5*het*hor)/comb(tot_pop,2)
print(prob_dom)
