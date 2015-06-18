
from urllib.request import urlopen

def find_pro_motif(string):
	position=[]
	for i in range(0, len(string)-3):
		if string[i] == 'N' and string[i+1] != 'P' and (string[i+2] == 'S' or string[i+2] =='T') and string[i+3]!= 'P':
			position.append(i+1)

	return position

def uni_fa(name):

	return "http://www.uniprot.org/uniprot/"+name.rstrip('\n')+".fasta"


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

	result={}
	try:
		f = open('data/rosalind_mprt.txt')
	except IOError:                     
		print ("The file, %s, does not exist" % filename)
		return

	for line in f:
		url = uni_fa(line)
		string = url_str(url)
		result[line.rstrip('\n')]=find_pro_motif(string)

	for key in result.keys():
		if result[key] != []:
			print (key)
			place=''
			for item in result[key]:
				place+=str(item)+' '
			print (place)

		


if __name__ == '__main__':
	main()