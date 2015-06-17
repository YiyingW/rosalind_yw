from scipy.misc import comb 
 
k = 7
N = 31
 
prob = 0.0
for i in range(N,2**k+1):
    prob += comb(2**k, i) * (0.25**i) * (0.75**(2**k-i))
 
print (prob)


# the main points in this problem:
# 1. knowing the usage of scipy.misc.comb
# 2. the probability of getting Aa when mating with Aa is 0.25 no matter the other partner is AA, Aa, or aa. 
