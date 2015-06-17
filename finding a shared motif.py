import FASTAparser as FA

def longest_common_substring(str1,str2):
	substring=''
	for i in range(0, len(str1)-1):
		for j in range(i, len(str1)):
			if str1[i:j] in str2 and len(str1[i:j]) > len(substring):
				substring = str1[i:j]

	return substring 


def main():
	DNAstrings=FA.FASTA('data/rosalind_lcsm.txt')

	DNAinlist = [value for value in DNAstrings.values()]
	DNAinlistsorted=sorted(DNAinlist, key = len)

	total = len(DNAinlistsorted)

	str1 = DNAinlistsorted[0]

	result = set()
	for i in range(0, len(str1)-1):
		for j in range(i+1, len(str1)):
			value = 1
			number =2
			while value == 1 and number <= total:
				if str1[i:j] not in DNAinlistsorted[number-1]:
					value = 0
				else: 
					number +=1 
			if value ==1:
				result.add(str1[i:j])
	result1 = sorted(result, key = len)

	print (result1)







if __name__ == '__main__':
	main()
