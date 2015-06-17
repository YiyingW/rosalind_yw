#!/usr/bin/python



def reverseDNA(DNA):
	intab ="ATCG"
	outtab ="TAGC"
	return DNA.translate({ord(x): y for (x,y) in zip(intab,outtab)})[::-1]

def DNAtoRNA(DNA):
	intab = "T"
	outtab = "U" 

	return DNA.translate({ord(x):y for (x,y) in zip(intab,outtab)})

def RNAtoProtein(RNA):
	protein = ''
	bases = ['U', 'C', 'A', 'G']
	codons = [a+b+c for a in bases for b in bases for c in bases]
	amino_acids = 'FFLLSSSSYY&&CC&WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	codon_table = dict(zip(codons, amino_acids))

	for i in range(0, len(RNA),3):
		if RNA[i:i+3] in codon_table.keys():
			protein+=codon_table[RNA[i:i+3]]



	return protein


def main():
	
	print (reverseDNA('ATCG'))


if __name__ == "__main__":
	main()

