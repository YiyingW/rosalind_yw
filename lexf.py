
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
	n = 4
	symbol_list =['E','C','J','U']
	result = all(n, symbol_list)
	for item in result[n]:
		print (item)



if __name__=='__main__':
	main()

