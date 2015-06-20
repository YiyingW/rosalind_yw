import math

def prob(DNA, A):
	B = []
	for cg in A:
		p = 1
		for i in range(0, len(DNA)):
			if DNA[i] == 'C' or DNA[i] =='G':
				p *= cg/2
			else:
				p *= (1-cg)/2
		B.append(math.log(p,10))
	return B

def main():

	DNA = 'AATCGCACATGTTTTGCGTAGTTTAGCGAACGCTGTGTGTGCACCGGTCCCCATCACGTATGTATATGAGTCCGTTTAGG'
	A = [0.090, 0.127, 0.192, 0.228, 0.307, 0.366, 0.402, 0.465, 0.536, 0.557, 0.631, 0.688, 0.753, 0.815, 0.879, 0.902]
	

	result = ''
	for item in prob(DNA, A):
		result += (str(item) +' ')
	print (result)






if __name__ == '__main__':
	main()