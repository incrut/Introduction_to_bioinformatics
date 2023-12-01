def Dna2Protein (seq, codon_table):

    protein = ""
    stop_codons = ["UGA", "UAG", "UAA"]

    rna_seq = seq.replace('T', 'U')

    codon_table_file = open(codon_table, "r")
    rows = codon_table_file.read().splitlines()
    codon_table_file.close()
    сodon_table_dict ={}

    for i in rows:
        cod, prot = map(str, i.split())
        сodon_table_dict[cod] = str(prot)

    for i in range (0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        if codon in stop_codons:
            break
        amino_acid = сodon_table_dict[codon]
        protein += amino_acid
    return protein


print (Dna2Protein("ATCACGGTCGCCCTGCGGATGTACTACCATGAAAGTTGATCACGTGCCGCGCGCTCCCTAAGCTTAGAAGTTTGCACAATCTGCATTCTATCCTGCCACGCCTTCAATAATAAGTGGTGTATGCAATTTGGA","RNAcodons.txt"))