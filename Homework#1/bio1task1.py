def RevCompl (seq):
    try:
        seq = seq.upper()
        new_seq = ""
        for i in range(1,len(seq)+1):
            target = seq[-i]
            if target == 'A':
                new_seq += 'T'
            elif target == 'T':
                new_seq += 'A'
            elif target == 'C':
                new_seq += 'G'
            elif target == 'G':
                new_seq += 'C'
            else:
                print ("Input sequence contains invalid characters")
                break
    except:
        print ("Your sequence is not correct")
    return new_seq


print(RevCompl("GTCGATCTGGGAACCAACGATTAACTTGGGAAGTGGCTATATCAAAATACGATGTCTTCAGCGTCGCGGTCGACGCTGCGCAACGAACGAAAAGTCCGATGGACCCGAACTCTGATTATACCGAATCTCCGC"))