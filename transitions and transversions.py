import FASTAparser as FA 


def t_t_ratio(s1,s2):
	length = len(s1)
	transition = 0
	transversion = 0
	same = 0
	for i in range(0, length):
		if (s1[i],s2[i]) == ('A','G') or (s1[i],s2[i]) == ('G','A') or (s1[i],s2[i]) == ('C','T') or (s1[i],s2[i]) == ('T','C'):
			transition +=1
		elif s1[i] == s2[i]:
			same += 1
		else:
			transversion += 1


	return (transition/transversion)






def main():
	DNAstrings=FA.FASTA('data/rosalind_tran.txt')

	alist=[]
	for value in DNAstrings.values():
		alist.append(value)


	
	print (t_t_ratio(alist[0],alist[1]))


if __name__ == '__main__':
	main()