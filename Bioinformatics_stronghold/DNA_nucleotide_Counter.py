
# Count the nucleotides in a string(s)
# Output should be four intergers seperated by spaces, counting A, C, G and T
# occuring in the dna string, s.


DNAstring = "GCAGTATCGCGACGAAGTATTCTTCTTGTGTATAGCTTGTGAGCACCATTCGTGCTATGACTGCGTTTACAGGGGTTGGCTGGATCATAGATCACGACGAAGCCCGAAGGTAGTTAAGATATCAAACAGCCCAATATGGGGCTAAATACCTGAAAGCTTGCTAAGCTGAACCAATCTCCACGATTACTACAACTATTCGTACAATTGCCCGACGTACTTGTTAATTCTCTCGAATCTAGCTCTGGTCCGCATTAAGCAGATCCATGATTAAAGTATGGACACAGTCTTGCCAACCTCGTAAACTCTGATCTCGGTCCGTAATTATGGAACCCTCTGGCGCCTCCTTGGAACAACATCCACGATGCCATGTCTAATTCCGTAGATCAGGACGTCATCTAGAAATCGGTCCTTGGTTACTGCAAAATTCGCTTGAGACGAAAGATAAGCTAGCTTCAAAGGCTCAACTCGTAATCCCCCAGAGCCACCATGATACCACCAAGCCATGCCTGGATATTAAGCGTGATCTCCAACTTCATTACGCGGCATGGCCCTGACTGCAACATCAAAGATGATACGAATTCGAATGTCACGCAGTGGTCAAGTTCACCCCACAAAATCCGCCGTTCCCGGCCGTGAAATCACCAGGTGGGATCTTACCTGTATTACGCGGAATGCTGTAACTGGCAGGGGAGCTTCGACGTCAGAGCGACACAGGCAGGCAGTCTATCCACCTTTATTGAATTGGGCTAAGACTATTCGCGCCCTAGTGCTGAGCCACACCCTTACTCTGAAATTGGCAACTTGCCTTTAACAGGGAAAGTATCTTTGATCGAT"


# First nucleotide counter
def DNAnucleotide_counter(seq): 
    """ Makes sure the string is upper case then counts each nucleotide."""        
    s = seq.upper()

    nucA = s.count("A")
    nucC = s.count("C")
    nucG = s.count("G")
    nucT = s.count("T")

    print(nucA, nucC, nucG, nucT)

DNAnucleotide_counter(DNAstring)
print("-------------")



# Second nucleotide counter
def DNA_nuc_counter(seq):
    """ make sure sequence is upper case only. Then starts counting by adding
    to the dictionary after each nucleotides. By unpacking the values we get the count."""
    
    seqUpper = seq.upper()     

    NucDict = {"A": 0, "C": 0, "G": 0, "T": 0}   # Dictionary of nucleotides at beginning of count

    for nucleotide in seqUpper:                  # For each specific nucleotide in the string
        NucDict[nucleotide] += 1                 # the value of that nucleotide increases by 1.
    
    print(*NucDict.values())                     # Unpacks a list into position arguments.              
   

DNA_nuc_counter(DNAstring)


