# =====================================================
# Functional Annotation of Hypothetical Protein FN1032
# Organism: Fusobacterium nucleatum
# Method: Homology-based annotation using BLAST
# =====================================================

from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

# -------------------------------
# STEP 1: Read FASTA sequence
# -------------------------------
record = SeqIO.read("sample.fasta", "fasta")

print("Protein ID:", record.id)
print("Description:", record.description)
print("Sequence Length:", len(record.seq))

# -------------------------------
# STEP 2: BLASTp analysis
# -------------------------------
print("\nRunning BLASTp against nr database...")

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
)

with open("blast_fn1032.xml", "w") as out_file:
    out_file.write(result_handle.read())

print("BLAST completed successfully.")

# -------------------------------
# STEP 3: Parse BLAST results
# -------------------------------
print("\nTop BLAST Hits:")

with open("blast_fn1032.xml") as result:
    blast_record = NCBIXML.read(result)

cvpa_hits = 0

for alignment in blast_record.alignments[:5]:
    hsp = alignment.hsps[0]
    print("Hit ID:", alignment.hit_id)
    print("Description:", alignment.hit_def)
    print("Identity:", hsp.identities)
    print("E-value:", hsp.expect)
    print("-" * 50)

    if "CvpA" in alignment.hit_def:
        cvpa_hits += 1

# -------------------------------
# STEP 4: Functional Annotation
# -------------------------------
print("\nFunctional Annotation Result:")

if cvpa_hits > 0:
    print("FN1032 is predicted to be a CvpA family protein.")
    print("Function assigned based on homology analysis.")
else:
    print("No known protein family identified.")
