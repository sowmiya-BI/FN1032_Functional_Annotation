# FN1032 Functional Annotation
Functional annotation of hypothetical protein FN1032 using Biopython and Bioinformatics tools

## Objective
To perform functional annotation of the hypothetical protein FN1032 from
Fusobacterium nucleatum using Biopython and BLAST.

## Input Data
- Protein sequence in FASTA format

## Methodology
1. Read protein sequence using Biopython
2. Perform BLASTp analysis against NCBI nr database
3. Analyze homologous sequences
4. Assign function based on sequence similarity
   
## Code Overview
This Python script performs functional annotation of the hypothetical protein
**FN1032 (CvpA family protein)** from *Fusobacterium nucleatum* using Biopython.

The code works as follows:
1. Reads the protein sequence from a FASTA file.
2. Runs BLASTp against the NCBI nr database.
3. Saves the BLAST output in XML format.
4. Parses BLAST results to identify homologous proteins.
5. Predicts protein function based on sequence similarity.

## Results
BLAST analysis revealed strong similarity to CvpA family proteins from
Fusobacterium species with very low E-values.

## Conclusion
Based on homology, FN1032 is predicted to be a CvpA family protein.
Experimental validation is required to confirm its biological role.

## Tools Used
- Python
- Biopython
- NCBI BLAST

