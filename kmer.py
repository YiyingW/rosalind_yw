import FASTAparser as FA

def all(n, symbol_list):
	dictionary={}
	dictionary[1] = symbol_list
	for i in range(2, n+1):
		dictionary[i] = []
		for symbol in range(0, len(symbol_list)):
			for item in dictionary[i-1]:
				dictionary[i].append(symbol_list[symbol]+item)


	return dictionary

def main():
	DNAstring = FA.FASTA('data/rosalind_kmer.txt')
	
	for item in DNAstring.values():
		DNA = item
		
	#DNA = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'

	k_mer = all(4, ['A','C','G','T'])[4]
	result = [0 for i in range(0, 256)]



	for i in range(0,len(DNA)-3):
		for j in range(0, 256):
			if DNA[i:i+4] == k_mer[j]:
				result[j]+=1

	
	printout =''
	for item in result:
		printout += str(item)+' '

	print (printout)


if __name__ == '__main__':
	main()