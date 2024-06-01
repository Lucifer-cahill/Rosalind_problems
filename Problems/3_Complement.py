data = open('rosalind_revc.txt').read()

data = 'CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG'        #Input string
comp = {'A':'T',                                                
'T':'A',                                                        #Dictionary to add complementary base to output strand
        'C':'G',                                                #while reading input strand
        'G':'C'}
output = ''
for i in data:                                                  #Loop for reading the data and generating an output strand
    if i in comp:                                               
        output = comp[i] + output                               #Adding the complementary base to the left of 
                                                                #output string to give reverse complement
print(output)



