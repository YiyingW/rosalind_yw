import itertools

def permutation(number):
	alist=[i for i in range(1, number+1)]
	return list(itertools.permutations(alist))

def main():
	print (len(permutation(7)))
	for item in permutation(7):
		result = ''
		for n in item:
			result+=str(n)+' '
		print (result)


if __name__=="__main__":
	main()