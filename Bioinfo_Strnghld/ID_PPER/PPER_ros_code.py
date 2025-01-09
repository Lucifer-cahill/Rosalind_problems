import math
data = open('ID_PPER\\rosalind_pper.txt').read()
# data = open('sample.txt').read()

input = [int(x) for x in data.split(' ')]

pper = math.factorial(input[0])/math.factorial(input[0]-input[1])
output = pper%1000000

# print(output)




# output = ' '.join([str(x) for x in output])
with open('ID_PPER\\PPER_output.txt', 'w') as f:
        f.write(str(output))