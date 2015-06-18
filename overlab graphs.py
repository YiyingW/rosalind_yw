import FASTAparser as FA


def overlapgraphs(k, DNAstrings):
	
	result ={}
	for key1 in DNAstrings.keys():
		for key2 in DNAstrings.keys():
			if key1 != key2 and DNAstrings[key1][-1*k:]== DNAstrings[key2][:k]:
				if key1 not in result.keys():
					result[key1]=[]
					result[key1].append(key2)
				else:
					result[key1].append(key2)

	return result





def main():

	DNAstrings=FA.FASTA('data/rosalind_grph.txt')
	result_dict = overlapgraphs(3, DNAstrings)
	for key in result_dict.keys():
		for item in result_dict[key]:
			print (key, item)

if __name__ == '__main__':
	main()