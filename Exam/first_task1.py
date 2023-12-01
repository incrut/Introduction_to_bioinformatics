# Import the Biopython module for sequence analysis
from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils import molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqUtils.IsoelectricPoint import IsoelectricPoint
from Bio.SeqUtils import ProtParam
import re

Entrez.email = "your_email@gmail.com"

protein_id = "DAA09395.1"
handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
seq = record.seq
protein_sequence = str(record.seq)

# Determine the length of the protein sequence
sequence_length = len(protein_sequence)
print("Protein sequence length:", sequence_length)

# Count the number of negatively charged amino acids
negatively_charged_aa = ["D", "E"]
count_negatively_charged = sum(
    protein_sequence.count(aa) for aa in negatively_charged_aa
)
print("Number of negatively charged amino acids:", count_negatively_charged)

# Find the positions of "VLLPP" docking sites
docking_site = "VLLPP"
docking_site_positions = []
start = 0
while start < sequence_length:
    position = protein_sequence.find(docking_site, start)
    if position == -1:
        break
    docking_site_positions.append(
        position + 1
    )  # Adding 1 to adjust for Python indexing
    start = position + 1

print("Docking site positions:", docking_site_positions)
