from urllib.request import urlopen

def url_str(url):

	response = urlopen(url)
	fasta = response.readlines()
	sequence = ''
	for line in fasta:
		if line.decode("utf-8").startswith('>'):
			sequence= ''
		else:
			sequence+= line.decode("utf-8").replace('\n','')
	return sequence
	

def main():
	url = "http://www.uniprot.org/uniprot/B5ZC00.fasta"
	print (url_str(url))


if __name__ == '__main__':
	main()
