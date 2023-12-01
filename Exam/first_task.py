from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils import molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqUtils.IsoelectricPoint import IsoelectricPoint
from Bio.SeqUtils import ProtParam
import re
from Bio.SeqUtils.ProtParam import ProteinAnalysis

Entrez.email = "your_email@gmail.com"

protein_id = "DAA09395.1"

handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
protein_sequence = str(record.seq)

print("Protein information:", record.description)

X = ProteinAnalysis(prot_sequence=protein_sequence)
aa_num = 0
aa_dict = X.count_amino_acids()
for key in aa_dict:
    aa_num += aa_dict[key]

print("Number of amino acids:", aa_num)
print("They are:", aa_dict)

negatively_charged_aa = ["D", "E"]
count_negatively_charged = sum(
    protein_sequence.count(aa) for aa in negatively_charged_aa
)
print("Number of negatively charged amino acids:", count_negatively_charged)

docking_site = "VLLPP"
docking_site_positions = []
start = 0
while start < len(protein_sequence):
    position = protein_sequence.find(docking_site, start)
    if position == -1:
        break
    docking_site_positions.append(position + 1)
    start = position + 1

print("Docking site positions:", docking_site_positions)
