
text=open('rosalind_sseq.txt')
data=text.read().replace('\n', '')
str1=''
i=14
while data[i] != '>':
	str1+=data[i]
	i+=1
i=i+14
str2=''
while i < len(data):
	str2+=data[i]
	i+=1


number=0
j=0
for j in range(0, len(str2)):
	while str2[j] != str1[number]:
		number+=1
	number+=1
	print (number,end=' ')


	
