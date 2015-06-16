import FASTAparser as FA
from statistics import mode


def map_position(adict):
	newdict={}
	for string in adict.values():
		for i in range(0, len(string)):
			if i not in newdict.keys():
				newdict[i]=[string[i]]
			else:
				newdict[i].append(string[i])

	return newdict





def main():
	DNAstrings=FA.FASTA('data/rosalind_cons.txt')

	result=''
	for value in map_position(DNAstrings).values():
		A,T,C,G=0,0,0,0
		for item in value:
			if item == 'A':
				A+=1
			elif item =='T':
				T+=1
			elif item == 'C':
				C+=1
			else:
				G+=1
		if A == max(A,T,C,G):
			result+='A'
		elif T == max(A,T,C,G):
			result+= 'T'
		elif C == max(A,T,C,G):
			result+='C'
		else:
			result+='G'


	print (result)

	
	



if __name__=="__main__":
	main()