from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils import molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqUtils.IsoelectricPoint import IsoelectricPoint
from Bio.SeqUtils import ProtParam
import re


Entrez.email = "your_mail@gmail.com"

protein_id = "DAA11591"

# Use Entrez to fetch the protein sequence with the given ID
handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
seq = record.seq
print("1) Description: ", record.description)
print("2) Sequence: ", seq)
print("3) Length: ", len(seq))


print(
    "4) Number of Positively Charged Amino Acids:",
    seq.count("R") + seq.count("H") + seq.count("K"),
)


mw = molecular_weight(record.seq, "protein") / 1000

print("5) Molecular Weight (kDa):", round(mw, 2))


protein_analysis = ProteinAnalysis(str(record.seq))
instability_index = protein_analysis.instability_index()

print("6) Instability Index:", round(instability_index, 2))


iep = IsoelectricPoint(str(seq))

print("7) Isoelectric Point:", round(iep.pi(), 2))


# pxl_pattern = re.compile("P[xX][Ll]")
# pxl_matches = pxl_pattern.finditer(str(seq))
# pxl_positions = []
# pxl_sequences = []
# for match in pxl_matches:
#     pxl_positions.append(match.start())
#     pxl_sequences.append(match.group())

# print("8) Number of PxL Sites:", len(pxl_positions))
# print("PxL Site Positions:", pxl_positions)
# print("PxL Site Sequences:", pxl_sequences)


protein_sequence = str(seq)
pxl_pattern = re.compile(r"P\wL")
pxl_matches = [
    (match.start(), match.group())
    for match in re.finditer(pxl_pattern, protein_sequence)
]
print("8) Cdc14 Docking Sites (PxL) Positions and Sequences:")

with Entrez.efetch(db="protein", rettype="fasta", id="DAA11591") as handle:
    seq_record = SeqIO.read(handle, "fasta")

sites1 = [pos for pos, char in enumerate(seq_record) if char == "P"]
sites2 = [pos for pos, char in enumerate(seq_record) if char == "P"]

for el in sites1:
    if seq_record[el + 2] == "L":
        out = str(el + 1)
        print(out, end=" ")
        print(seq[el : el + 3])


phospho_sites = []
for i in range(len(protein_sequence) - 1):
    if protein_sequence[i : i + 2] == "SP" or protein_sequence[i : i + 2] == "TP":
        position = i + 1
        sequence = protein_sequence[i : i + 2]
        phospho_sites.append((position, sequence))

if phospho_sites:
    print("9) Cdk1 Phosphorylation Sites (SP/TP):")
    for site in phospho_sites:
        print("  - Position:", site[0], "Sequence:", site[1])
else:
    print("9) No Cdk1 Phosphorylation Sites (SP/TP) found in the protein sequence.")


optimal_cdk1_pattern = re.compile(r"(S|T)[^P][RK][^P]")
optimal_cdk1_matches = [
    (match.start(), match.group())
    for match in re.finditer(optimal_cdk1_pattern, protein_sequence)
]
print(
    "10) Optimal Cdk1 Phosphorylation Sites (SPxK/R or TPxK/R) Positions and Sequences:"
)
for aa in sites2:
    if seq_record[aa - 1] == "S" or seq_record[aa - 1] == "T":
        if seq_record[aa + 2] == "R" or seq_record[aa + 2] == "K":
            print(aa, ":", seq[aa - 1 : aa + 3])
