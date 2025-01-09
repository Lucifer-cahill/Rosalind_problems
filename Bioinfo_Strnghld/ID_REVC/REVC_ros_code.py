data = open('rosalind_revc.txt').read()

comp = {'A':'T',                                                
        'T':'A',                                                        
        'C':'G',                                                
        'G':'C'}

output = ''
for i in data:                                                 
    if i in comp:                                               
        output = comp[i] + output                               
print(output)



