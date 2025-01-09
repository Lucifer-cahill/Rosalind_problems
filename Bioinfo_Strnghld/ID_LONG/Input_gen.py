import random
supstr = "".join(random.choice('AGCT') for _ in range(50))
print(supstr)

frag_lst = []

for i in range(10):
    frag_lst.append(supstr[4*i:4*i + 10])
# print(frag_lst)
random.shuffle(frag_lst)
print(frag_lst)

# output = ' '.join([str(x) for x in ])
# with open('LGIS_output.txt', 'w') as f:
#       f.write(output)