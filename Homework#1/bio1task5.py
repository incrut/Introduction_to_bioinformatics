def HamDist(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("sequences must be of equal lengths")
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist

def MotifMatchMismach (dna_seq, pattern, d):
    match_list = []
    for i in range (len(dna_seq)-len(pattern)):
        curr_seq = dna_seq[i:]
        if HamDist(curr_seq[0:len(pattern)], pattern) <= d:
                match_list.append(i+1)
    return match_list


test = MotifMatchMismach("CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC","CCGTCATCC",3)

print (test)