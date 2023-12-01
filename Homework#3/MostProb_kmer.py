def most_prob_kmer(text, k, profile):
    max_prob = -1
    most_probable_kmer = ''
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            if kmer[j] == 'A':
                prob *= profile[0][j]
            elif kmer[j] == 'C':
                prob *= profile[1][j]
            elif kmer[j] == 'G':
                prob *= profile[2][j]
            elif kmer[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer


"""HOMEWORK"""

inp = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA 12 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.1 0.2 0.3 0.4 0.5 0.3 0.2 0.1 0.1 0.2 0.1 0.1 0.4 0.3 0.2 0.2 0.1 0.2 0.1 0.4 0.3 0.1 0.1 0.1 0.3 0.1 0.1 0.2 0.1 0.3 0.4 0.1 0.1 0.1 0.1 0.0 0.2 0.4 0.4 0.2 0.3"

new_inp = inp.split()

dna = new_inp[0]
k = int(new_inp[1])
profile = list(range(4))  #list with the size of 4

for i in range (4):   #filling the list with the values from the input string
    profile [i] = new_inp[2+(i*k):k+2+(i*k)]

for i in range(len(profile)):   #str to float convertation
    for j in range (len(profile[i])):
        profile[i][j] = float(profile[i][j])


"""TEST"""

test_inp = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT 5 0.2 0.2 0.3 0.2 0.3 0.4 0.3 0.1 0.5 0.1 0.3 0.3 0.5 0.2 0.4 0.1 0.2 0.1 0.1 0.2"


new_test_inp = test_inp.split()

test_dna = new_test_inp[0]
test_k = int(new_test_inp[1])
test_profile = list(range(4))  #list with the size of 4

for i in range (4):   #filling the list with the values from the input string
    test_profile [i] = new_test_inp[2+(i*test_k):test_k+2+(i*test_k)]

for i in range(len(test_profile)):   #str to float convertation
    for j in range (len(test_profile[i])):
        test_profile[i][j] = float(test_profile[i][j])



print (most_prob_kmer(dna, k, profile))
print(most_prob_kmer(test_dna, test_k, test_profile))