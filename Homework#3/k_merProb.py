def kmer_probability(dna, k, profile):

    for i in range(len(dna)):
        if dna[i] == 'A':
            p = profile[0][i]
        elif dna[i] == 'C':
            p = profile[1][i]
        elif dna[i] == 'G':
            p = profile[2][i]
        elif dna[i] == 'T':
            p = profile[3][i]
        
        try:
            prob = prob*p
        except:
            prob = p

    try:
        return prob*1000
    except:
        return "Something went wrong" 

inp = "ATGAAGACTTTA 12 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.1 0.2 0.3 0.4 0.5 0.3 0.2 0.1 0.1 0.2 0.1 0.1 0.4 0.3 0.2 0.2 0.1 0.2 0.1 0.4 0.3 0.1 0.1 0.1 0.3 0.1 0.1 0.2 0.1 0.3 0.4 0.1 0.1 0.1 0.1 0.0 0.2 0.4 0.4 0.2 0.3"

test_inp = "CCGAG 5 0.2 0.2 0.3 0.2 0.3 0.4 0.3 0.1 0.5 0.1 0.3 0.3 0.5 0.2 0.4 0.1 0.2 0.1 0.1 0.2"

new_inp = inp.split()
new_test_inp = test_inp.split()

dna = new_inp[0]
k = int(new_inp[1])
profile = list(range(4))  #list with the size of 4

test_dna = new_test_inp[0]
test_k = int(new_test_inp[1])
test_profile = list(range(4))  #list with the size of 4
"""HOMEWORK"""
for i in range (4):   #filling the list with the values from the input string
    profile [i] = new_inp[2+(i*k):k+2+(i*k)]

for i in range(len(profile)):   #str to float convertation
    for j in range (len(profile[i])):
        profile[i][j] = float(profile[i][j])
"""TEST"""
for i in range (4):   #filling the list with the values from the input string
    test_profile [i] = new_test_inp[2+(i*test_k):test_k+2+(i*test_k)]

for i in range(len(test_profile)):   #str to float convertation
    for j in range (len(test_profile[i])):
        test_profile[i][j] = float(test_profile[i][j])

print (kmer_probability(dna, k, profile))
print(kmer_probability(test_dna, test_k, test_profile))