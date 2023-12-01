def MotifMatch (dna_seq, pattern):
    match_counter = 0
    for i in range (len(dna_seq)-len(pattern)):
        curr_seq = dna_seq[i:]
        if curr_seq[0:len(pattern)] == pattern:
                match_counter += 1
    return match_counter


test = MotifMatch("TCGGATTAACCCAGATTAACTTACGATTAACGGATTAACGATTAACCGATTAACACTCGGCGGGCGATTAACTATACGTAATTATTCAGTGATTAACCTATAGCCGATTAACGATTAACGATTAACCCGATTAACGCGATTAACGATTAACGCGATTAACCTGATTAACCGATTAACTTGATTAACGATTAACGATTAACATCGTCGGATTAACGATTAACGGACGATTAACAAGGATTAACGTTTGATTAACTTCGGTCTCGATTAACCTGATTAACAGATTAACCTGATTAACGATTAACCGTCGGCGATTAACTGTTGATTAACTAGGGATTAACAAATCGATTAACGATTAACGGGATTAACAGAAAAGATTAACTCGATTAACCCCACGTGATTAACGAGAGCCGGAGATTAACGATACCTCACGTACGCATGGATTAACTTGATTAACAGATGATTAACCGGATTAACTTGCCTGATTAACGATTAACTGATTAACGATTAACGAGATTAACGATTAACGATTAACAGGTGATTAACAATTGCGGATTAACTGATTAACTGTTCGATTAACTCTGATTAACGGATTAACGATTAACCGATTAACAACGTATGGATTAACGGAGATTAACTGATTAACGCATGCTATTTTTATGGGATTAACGATTAACAATAAAGATTAACCTCTCGATTAACGATTAACGGATTAACTAGCTAAGATTAACGTAATCTGCGCTTGGGCACAATCGATTAACTTATGATTAACTGATTAACCGGATTAACACGATTAACCCAGATTAACAAGTTGATTAACGTTGATGTGATTAACGTTGGAAGATTAACGGATTAACCCGATTAACATGATTAACAGATTAACATGATTAACTTGGATTAACAGGATTAACGCAGATTAACGATTAACCGATTAAC","GATTAACGA")

print (test)