data = open('rosalind_iev.txt')
for i in data.readlines():
    input = i.split(' ')
    c_1 = int(input[0])
    c_2 = int(input[1])
    c_3 = int(input[2])
    c_4 = int(input[3])
    c_5 = int(input[4])
    c_6 = int(input[5])

exp = 2*(c_1 + c_2 + c_3 + 0.75*c_4 + 0.5*c_5)

print(exp)
