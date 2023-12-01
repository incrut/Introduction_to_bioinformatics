def consensus(motif):
    n = len(motif[0]) # length of each DNA string in the motif
    counts = [] # list of dictionaries with the counts of each nucleotide in each column
    for j in range(n):
        column = [motif[i][j] for i in range(len(motif))] # extract the j column of the motif
        counts.append({nuc: column.count(nuc) for nuc in "ACGT"}) # count the occurrences of eachg nucleotide in the column
    consensus = "".join([max(counts[j], key=counts[j].get) for j in range(n)]) # making the consensus string
    return consensus


motf_str = "CATGGGGAAAACTGA CCTCTCGATCACCGA CCTATAGATCACCGA CCGATTGATCACCGA CCTTGTGCAGACCGA CCTTGCCTTCACCGA CCTTGTTGCCACCGA ACTTGTGATCACCTT CCTTGTGATCAATTA CCTTGTGATCTGTGA CCTTGTGATCACTCC AACTGTGATCACCGA CCTTAGTATCACCGA CCTTGTGAAATCCGA CCTTGTCGCCACCGA TGTTGTGATCACCGC CACCGTGATCACCGA CCTTGGTTTCACCGA CCTTTGCATCACCGA CCTTGTGATTTACGA"
motif = motf_str.split()

consensus_out = consensus(motif)
print("Consensus string:", consensus_out)