# dict key is name of sequence, value is the sequence


def FASTA(filename):
  try:
    f = open(filename)
  except IOError:                     
    print ("The file, %s, does not exist" % filename)
    return

  order = []
  sequences = {}
    
  for line in f:
    if line.startswith('>'):
      name = line[1:].rstrip('\n')
      name = name.replace('_', ' ')
      order.append(name)
      sequences[name] = ''
    else:
      sequences[name] += line.rstrip('\n').rstrip('*')
            
  print ("%d sequences found" % len(order))
  return sequences


def main():
  dic = FASTA('rosalind_sseq.txt')
  for item in dic.values():
    print (item)


if __name__=="__main__":
  main()