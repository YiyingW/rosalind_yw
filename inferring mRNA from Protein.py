def ProteintoRNA():
	
	bases = ['U', 'C', 'A', 'G']
	codons = [a+b+c for a in bases for b in bases for c in bases]
	amino_acids = 'FFLLSSSSYY&&CC&WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	codon_table = dict(zip(codons, amino_acids))

	Pro_RNA={}
	for key in codon_table.keys():
		if codon_table[key] not in Pro_RNA.keys():
			Pro_RNA[codon_table[key]]=[]
			Pro_RNA[codon_table[key]].append(key)
		else:
			Pro_RNA[codon_table[key]].append(key)


	return (Pro_RNA)


def main():

	Pro_RNA_dic = ProteintoRNA()
	ProteinString='MVVPEINPQCFMNIAKSAYDGCPVTNFTCPGLYMNFQGGLDKRIYDIQAREHIVNQATCCMWRAWGTRICENKLFPLDWKEEFKNAIGFLPCCFTPYCMTKTYWWKCVWSWNKKVKILDKHITPAGRRWDDAHGPQGLFYITSQMARHWLHQQANNAIMPQVFFLIASGMMMPYAESRVKQCVDKCSAHCQKMEFTQIAVYSIETLNTITVIVCSMIMPAVHRVIKAFCIWWHWWDFRLFNTKPVMSKVGPGWVINNWRLFFCSSRQNLSMMHYTYLIYLIETREIDVGTDVSKCASRYDWTMFLPWDMRWQPMMVQTQNACLSVAAHTHVSYMHFWNKHSMYDAWWFHQVAYHTNNTDDGDDEHEADSIHAPPYCEHLNSYYAIRRQKTLAYMHGRLYPWKTGNCWPCWEEMTWGHLVQNVIIALTKKTKRWWGHNYVVPMPWRWFMRIVYCKLQIQCAVMVWIMLWGCNWRMYNFDSWWTIYLFCRCPVQPIPDPKVILHEAEAVTDHHCFMVTGKHGQSWFWTIRHWAFWQLGNMPPCRAFGYRGKFPNKAFSQWTVWYKTGAYQSAPWDKGHLMDCLRQYWDHPQCLNTQFWYEQMSSADCSSWWRKMDHALTLAINPGSYCGDYVSGGYPWMQKVFIGCRKGYHKDSVIHKCWVYEPCIQWRIDQNNAVLAITNFMGMYHKIRGADYLDSARYRKRVAQEHGWRKDLAKEQDGAICCNWRYGVPKEGLFRTVLMMECHVMYLYNCENVGQTNSFNASHCTEQWCFHSFLEGNFCCYVKCWTSGSERSEHRINAYFPKKIGGHRPRFMHREKAAYEGQIVITCPNKNWAASQYCDYFWHQPLQCIRKTDEIYNCGRAVSLMYNRHMENNRRPVMGPCWDTIAHPLHKAHTERYKKHVPIRNLGIGDTKSVWNVQMAKFDGTEVMMFATEAMMSSQINRTCMCFKCSYHDHAKVVEIHSFDIWVAEYTETSGTTHLAHRQREAWHEVMLKWGLRKVH'
	number = 3
	for i in range(0, len(ProteinString)):
		number = number * len(Pro_RNA_dic[ProteinString[i]])
		if number > 1000000:
			number = number % 1000000
	print (number)


if __name__=='__main__':
	main()