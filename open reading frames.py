from DNA_RNA import *
from FASTAparser import *
import re

def reading_frames(DNA):
	frames = {}
	frames[1] = DNA
	frames[2] = DNA[1:len(DNA)-2]
	frames[3] = DNA[2:len(DNA)-1]
	frames[4] = reverseDNA(DNA)
	frames[5] = reverseDNA(DNA)[1:len(DNA)-2]
	frames[6] = reverseDNA(DNA)[2:len(DNA)-1]

	return frames

def get_raw_protein(frames):
	raw_protein={}
	raw_protein[1] = RNAtoProtein(DNAtoRNA(frames[1]))
	raw_protein[2] = RNAtoProtein(DNAtoRNA(frames[2]))
	raw_protein[3] = RNAtoProtein(DNAtoRNA(frames[3]))
	raw_protein[4] = RNAtoProtein(DNAtoRNA(frames[4]))
	raw_protein[5] = RNAtoProtein(DNAtoRNA(frames[5]))
	raw_protein[6] = RNAtoProtein(DNAtoRNA(frames[6]))
	
	return raw_protein

def main():
	for value in FASTA('rosalind_orf.txt').values():
		DNAstring = value
	# dictionary of 6 possible frames
	DNA_reading_frames = reading_frames(DNAstring)
	#DNA_reading_frames=reading_frames('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
	
	raw_protein = get_raw_protein(DNA_reading_frames)
	result=set()
	for string in raw_protein.values():
		for i in range(0,len(string)):
			for j in range(i,len(string)):
				if string[i]=='M' and string[j]=='&':
					s=''
					for k in range(i,j):
						s=s+string[k]
					if '&' not in s:
						result.add(s)

	for item in result:
		print (item)






	

if __name__=="__main__":
	main()