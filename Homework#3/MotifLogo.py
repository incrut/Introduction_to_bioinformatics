import numpy as np

# Define the frequencies
freqs = {'A': [0, 0.4, 0.2, 0.8, 0, 0, 0, 0],
         'C': [0.2, 0.6, 0.6, 0.2, 0.2, 0, 0.2, 0],
         'G': [0, 0, 0, 0, 0.8, 1, 0.2, 1],
         'T': [0.8, 0, 0.2, 0.2, 0.8, 0, 0.6, 0]}

# Define the DNA sequences
sequences = ['TCTCGGGG',
             'CCAAGGTG',
             'TACAGGCG',
             'TACAGGTG',
             'TCCACGTG']

# Calculate the information content at each position
info_content = []
for i in range(len(sequences[0])):
    col_freqs = [freqs[nt][i] for nt in ['A', 'C', 'G', 'T']]
    col_info = sum([-x*np.log2(x) if x != 0 else 0 for x in col_freqs])
    info_content.append(2 - col_info)

# Create the sequence string for WebLogo
seq_string = ''
for i in range(len(sequences[0])):
    for j in range(len(sequences)):
        seq_string += sequences[j][i]
    seq_string += '|'

# Print the sequence string and the information content at each position
print(seq_string)
print(' '.join([str(round(ic, 2)) for ic in info_content]))
