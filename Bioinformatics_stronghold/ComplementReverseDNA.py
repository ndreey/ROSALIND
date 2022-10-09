


# DNA string shall be converted into its reversed compliment DNA string.
DNAstring = "TCCATCGTTCCCTTAAGGGGACTCGCCGTTCCCTGAAA"
def DNAtoReverseDNA(seq):

    s = seq.upper()
    compli_dna = []
    reverse_complimentDNA = {"A": "T", "C": "G", "G": "C", "T": "A"}

    for nuc in s:
        compli_dna.append(reverse_complimentDNA[nuc])
    compli_dna.reverse()
    print(*compli_dna, sep="")

    
DNAtoReverseDNA(DNAstring)


