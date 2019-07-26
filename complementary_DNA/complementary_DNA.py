"""Switch uppercase char A to T and G to C"""


def dna_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))

print('GCTA ==>', dna_strand("GCTA"))
