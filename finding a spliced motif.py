import FASTAparser as FA


def splice(str1,str2):
	position =[]
	str1_pointer = -1
	for i in range(0, len(str2)):
		str1_pointer +=1 
		while str1[str1_pointer] != str2[i]:
			str1_pointer += 1
		position.append(str1_pointer + 1)

	return position 


def main():

	DNAstrings=FA.FASTA('data/rosalind_sseq.txt')
	
	alist=[]
	for value in DNAstrings.values():
		alist.append(value)

	result = ''
	for item in (splice(alist[0], alist[1])):
		result += (str(item) +' ')
	print (result)



if __name__ == '__main__':
	main()






	
