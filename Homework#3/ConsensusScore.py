def consensus_score(motif):
    n = len(motif[0]) # length of each DNA string in the motif
    counts = [] # list of dictionaries with the counts of each nucleotide in each column
    for j in range(n):
        column = [motif[i][j] for i in range(len(motif))] # extract the j column of the motif
        counts.append({nuc: column.count(nuc) for nuc in "ACGT"}) # count the occurrences of each nucleotide in the column
    consensus = "".join([max(counts[j], key=counts[j].get) for j in range(n)]) # make the consensus string
    score = sum([sum([counts[j][nuc] for nuc in "ACGT" if nuc != consensus[j]]) for j in range(n)]) # count the score
    return score


motf_str = "CATGGGGAAAACTGA CCTCTCGATCACCGA CCTATAGATCACCGA CCGATTGATCACCGA CCTTGTGCAGACCGA CCTTGCCTTCACCGA CCTTGTTGCCACCGA ACTTGTGATCACCTT CCTTGTGATCAATTA CCTTGTGATCTGTGA CCTTGTGATCACTCC AACTGTGATCACCGA CCTTAGTATCACCGA CCTTGTGAAATCCGA CCTTGTCGCCACCGA TGTTGTGATCACCGC CACCGTGATCACCGA CCTTGGTTTCACCGA CCTTTGCATCACCGA CCTTGTGATTTACGA"
motif = motf_str.split()

consensus_score_out = consensus_score(motif)
print("Consensus score:", consensus_score_out)