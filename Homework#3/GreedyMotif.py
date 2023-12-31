import random

def profile_with_pseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    count = [[1 for j in range(k)] for i in range(4)]
    for i in range(t):
        for j in range(k):
            if motifs[i][j] == 'A':
                count[0][j] += 1
            elif motifs[i][j] == 'C':
                count[1][j] += 1
            elif motifs[i][j] == 'G':
                count[2][j] += 1
            elif motifs[i][j] == 'T':
                count[3][j] += 1
    profile = [[float(count[i][j])/float(t+4) for j in range(k)] for i in range(4)]
    return profile

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

def score(motifs):
    t = len(motifs)
    k = len(motifs[0])
    count = 0
    for j in range(k):
        col = [motifs[i][j] for i in range(t)]
        count += t - max([col.count('A'), col.count('C'), col.count('G'), col.count('T')])
    return count

def randomized_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        start = random.randint(0, len(dna[i]) - k)
        best_motifs.append(dna[i][start:start+k])
    while True:
        profile = profile_with_pseudocounts(best_motifs)
        motifs = [most_prob_kmer(dna[i], k, profile) for i in range(t)]
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

def greedy_motif_search(dna, k, t):
    best_motifs = randomized_motif_search(dna, k, t)
    while True:
        profile = profile_with_pseudocounts(best_motifs)
        motifs = [most_prob_kmer(dna[i], k, profile) for i in range(t)]
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


test_inp = "8 5 CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
test_new_inp = test_inp.split()
test_k, test_t = int(test_new_inp[0]), int(test_new_inp[1])
dna = test_new_inp[2:]
best_motifs = greedy_motif_search(dna, test_k, test_t)
for i in range(999):
    motifs = greedy_motif_search(dna, test_k, test_t)
    if score(motifs) < score(best_motifs):
        best_motifs = motifs
print(' '.join(best_motifs))

inp = "15 20 ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT"
new_inp = inp.split()
k, t = int(new_inp[0]), int(new_inp[1])
dna = new_inp[2:]
best_motifs = greedy_motif_search(dna, k, t)
for i in range(999):
    motifs = greedy_motif_search(dna, k, t)
    if score(motifs) < score(best_motifs):
        best_motifs = motifs
print(' '.join(best_motifs))



def profile_matrix(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = [[0]*k for i in range(4)]
    for i in range(t):
        for j in range(k):
            if motifs[i][j] == 'A':
                profile[0][j] += 1
            elif motifs[i][j] == 'C':
                profile[1][j] += 1
            elif motifs[i][j] == 'G':
                profile[2][j] += 1
            elif motifs[i][j] == 'T':
                profile[3][j] += 1
    return profile

def most_prob_kmer(text, k, profile):
    n = len(text)
    max_prob = -1
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        prob = 1
        for j in range(k):
            if pattern[j] == 'A':
                prob *= profile[0][j]
            elif pattern[j] == 'C':
                prob *= profile[1][j]
            elif pattern[j] == 'G':
                prob *= profile[2][j]
            elif pattern[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            kmer = pattern
    return kmer

def score(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = profile_matrix(motifs)
    consensus = ''
    count = 0
    for j in range(k):
        m = 0
        freq = {'A':0, 'C':0, 'G':0, 'T':0}
        for i in range(t):
            freq[motifs[i][j]] += 1
            if freq[motifs[i][j]] > m:
                m = freq[motifs[i][j]]
                popular = motifs[i][j]
        consensus += popular
        count += t - m
    return count

def randomized_motif_search(dna, k, t):
    motifs = []
    for i in range(t):
        n = len(dna[i])
        rand_start = random.randint(0, n-k)
        motifs.append(dna[i][rand_start:rand_start+k])
    best_motifs = motifs
    while True:
        profile = profile_matrix(motifs)
        motifs = [most_prob_kmer(dna[i], k, profile) for i in range(t)]
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

def repeat_rms(dna, k, t, n):
    best_motifs = randomized_motif_search(dna, k, t)
    for i in range(n-1):
        motifs = randomized_motif_search(dna, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

inp = "15 20 ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT"
new_inp = inp.split()
k, t = int(new_inp[0]), int(new_inp[1])
dna = new_inp[2:]
best_motifs = repeat_rms(dna, k, t,1000)
print(' '.join(best_motifs))