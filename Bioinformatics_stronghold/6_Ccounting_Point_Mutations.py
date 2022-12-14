"""
Given:  Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).    (Number of mismatchs)

Solved: Jan. 28, 2021, 8:23 a.m.
"""

def pointMutations_counter(seq1,seq2):
    """
    By increasing the index value, the loop will check every index in the sequence and compare with
    each other. the loop will continue till all indexes in the string have been compared. 
    """

    index_value = 0
    loop_limit = len(seq1)
    loop_number = 0
    numb_mutations = 0

    while loop_number < loop_limit:
        if seq1[index_value] != seq2[index_value]:
            numb_mutations += 1
            index_value += 1
            loop_number += 1
        else:
            index_value += 1
            loop_number += 1 
    print(numb_mutations)
 

DNA_string1 = "ACACTAGAGGACGTGTCGTACTCCCGCACGTGTAAGAGGATCAGCAGTCTGTTTAGGCACTAAGGGGTTATATGGTCACTGGTTTTCTACTCACTAATAATAGCGATCACCCACGTTGATGACCCAGTTTCGTGTCCTGTATTGGTAGCAGAAAGGTCAGCTCAGGTTGTGACGTGCCCTTACCCTAGGGGGGCAACACCATAATCGTATGGATTATAACTGTCAGTAGGATATCTGGATATCGAACAGCAGTACCCGAGTTACAGCTGGTTTAGCGGCATCGACACCCCCCGCACCCGACTTATGTAGTTTTCAGCTCAAACAGTGGCTGTAGTAACAGCAGGAAGCTATTTACTTACGGCGACGCGAGATTATAAAAGACCCCGTTCTTCTGATGCCATCTGGCTTACTGAAGAGGAACCGTATATTACAGGCAATCCTCCTATTAGCGAAGGAGCTCCAGCTACTAGGATTTACTTCAATTAGTGGAATGGATGCCGAAAGGGATTCCTTGTCCCATGCTCGCTCTAACCACCATGGGTATGCGAAGTAGGATATGATCTTCCATATGTAATCTATTATCCGAGCGGAGCCGCGAACGGAGTTTAGGTGTAAGACAGCGCATCTGGGCTTGTGCTAAATCCTTGGGCTGGGATACGGTTAGAGCGGGAAGTACACCCCACATAAACCTATAGATAATTATGAAGGCAGACCCCCCCGCGAGGCACCCGGAATGATAAAGGTTGCTACCTTAGACCCCAGCCCGCCGCAACGACGAAACGGCCGTGCGTGGTCGGCACCAATTGTTTGATGCGCCTACTACATACCGACGATAGCTAGAGCAACAAATCTGGTTGAAGTGTCCAGTGGCTGAGAGTACTCTCTCCCAGGGCCTGGATGGATCAGTTTTAGTACGAGAACGCCTGGGTCCTAGGG".upper()
DNA_string2 = "GGGTGCTCACACGGGGAATATTCTCCGAATGACATGGGGGTCATCTGCTAATATACTCACTACGGGAAAATTTCGCATGGGCTTTTGTTGTAGCCAACGACTCCAACACAGCACATCGATACAAATGGTTTGTCCTCTTATTTCAATGTAATATGATGAACTCAGGAGGCGGTATGCCATCAAGCATGGCGGGAAGCAAGTTACCCGTACGGCCTCTACAAGTCATTAGTATGATTGAGCTACGACGGGTTGTGCGTTTTATTAACGTGGTTGTGAGCGATCAACAGGCAATTCCCTCATCAAACCTAATTTCTAGCACTGACTGAGCATATTCTACATGAGGAACCCTGTCGCACGACGGCTGAGAGTTAAAGAAATATGATGGGTTCCTCTCGTCGCATATCGCCTACGGAAGAGGAATAGCTTGCCATAGGCGCCTACAATCTTATCCTATGAGTACCGGCTAGGCTGCGTTACTACAGTAATTGCTTTGATCCTCTCTATCGACTTCCATTCCAATTGACTCTGGCATCAGGGTCGATATATAAGGTAGGAAATGATCATTGCTATCCCAAGTGTTATCCTAGAGAATCCGGTGATGAGCAGCATGTCTCATACAGTACTGCTGGGGATTAAGTAATTACCATTTGGACCACATCTAGTGAGCCGGAAGGACGATTCCCATAAAAAGACGGATAATTAAGTAGGGCGGTCAACTGGCTGAGTTTCATGAATTAGAACGATCGATGCCGCTGCCTCCAGTCTGCCGTACGACGCAAGAGTCCCCCCGTTTCCTGTACCTAATGTTAATTTGTCCACTTCGACGATTAACTTGGGTACACACACACGTTAGGGTCACCTGCACATTGACTCACAGTAGTAGCTCCGCGGGGTCGGACGGATCGGTTTGAGTAGGATCGGGTCCTCAGGCCGCGG".upper()


pointMutations_counter(DNA_string1, DNA_string2)
