from scipy.misc import comb as choose
 
k = 7
N = 31
 
prob = 0.0
for i in range(N,2**k+1):
    prob += choose( 2**k, i) * (0.25**i) * (0.75**(2**k-i))
 
print (prob)