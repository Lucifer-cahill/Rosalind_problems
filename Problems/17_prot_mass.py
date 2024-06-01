
mass_data = open('mass_table.txt').read()
mass_table = {}
prot = ''
for i in mass_data:
    if i != '\n' and i != ' ':
        prot += i
    if i == '\n':
        mass_table[prot[0]] = float(prot[1:])
        prot = ''
mass_table[prot[0]] = float(prot[1:])

print(mass_table)

data = open('rosalind_prtm.txt').read()

mass = 0
for i in data:
    if i in mass_table:
        mass += mass_table[i]

print(mass)