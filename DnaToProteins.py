# Converts a dna sequence to mrna
def convertToMrna(seq):
    mrna = ""
    for x in range(len(seq)):
        if seq[x] == 'A':
            mrna = mrna + 'U'
        elif seq[x] == 'G':
            mrna = mrna + 'C'
        elif seq[x] == 'C':
            mrna = mrna + 'G'
        elif seq[x] == 'T':
            mrna = mrna + 'A'
    return mrna

# Finds the index of the 'G' in the start codon
def findStartCodon(seq):
    for x in range (2, len(seq)):
        if seq[x] == 'G' and seq[x-1] == 'U' and seq[x-2] == 'A':
            return x
    return "No start codon found"

# Returns a 3 letter codon based on the given start index
def getCodon(start, seq):
    return seq[start : start + 3]

# Finds the amino acid that corresponds to the given codon
# The amino acids are organized in a 3D list
# Each list is organized like so [U, C, A, G]
# For each level of the list, 
def findAminoAcid(codon):
    indices = []
    for x in range (len(codon)):
        indices.append(findIndex(codon[x]))
    secondBase = firstBase[indices[0]]
    thirdBase = secondBase[indices[1]]
    return thirdBase[indices[2]]

# Given a mrna letter, returns the corresponding index
def findIndex(letter):
    if letter == 'U':
        return 0
    elif letter == 'C':
        return 1
    elif letter == 'A':
        return 2
    elif letter == 'G':
        return 3
    return -1

uu = ["Phenylalanine", "Phenylalanine", "Leucine", "Leucine"]
cu = ["Serine", "Serine", "Serine", "Serine"]
ua = ["Tyrosine", "Tyrosine", "Stop", "Stop"]
ug = ["Cysteine", "Cysteine", "Stop", "Tryptophan"]

cu = ["Leucine", "Leucine", "Leucine", "Leucine"]
cc = ["Proline", "Proline", "Proline", "Proline"]
ca = ["Histidine", "Histidine", "Glutamine", "Glutamine"]
cg = ["Arginine", "Arginine", "Arginine", "Arginine"]

au = ["Isoleucine", "Isoleucine", "Isoleucine", "Methionine"]
ac = ["Threonine", "Threonine", "Threonine", "Threonine"]
aa = ["Asparagine", "Asparagine", "Lysine", "Lysine"]
ag = ["Serine", "Serine", "Arginine", "Arginine"]

gu = ["Valine", "Valine", "Valine", "Valine"]
gc = ["Alanine", "Alanine", "Alanine", "Alanine"]
ga = ["Aspartic acid", "Aspartic acid", "Glutamic acid", "Glutamic acid"]
gg = ["Glycine", "Glycine", "Glycine", "Glycine"]

u = [uu, cu, ua, ug]
c = [cu, cc, ca, cg]
a = [au, ac, aa, ag]
g = [gu, gc, ga, gg]

firstBase = [u, c, a, g]

# Get dna sequence from file
fileName = input("Enter the file name: ")
dnaFile = open(fileName, "r")
dnaSequence = dnaFile.readline()

# convert dna sequence to messanger rna sequence
mrna = convertToMrna(dnaSequence)
# find the index of the start codon
startIndex = findStartCodon(mrna) + 1
# add the amino acids to a list
sequence = []
sequence.append("Methionine")
while (startIndex + 3) < len(dnaSequence):
    codon = mrna[startIndex : startIndex + 3]
    sequence.append(findAminoAcid(codon))
    startIndex += 3
print(sequence)
