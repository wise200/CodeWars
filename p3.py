from math import sqrt

def sieve(n):
	primes = [True] * (n+1)
	for i in range(2,int(sqrt(n)+1)):
		if primes[i]:
			for comp in range(2*i,n+1,i):
				primes[comp] = False
	primes = [x for x in range(2,n+1) if primes[x]]
	return primes
	
def mag(n, primes):
	string = str(n)
	for x in range(1,len(string)):
		if int(string[:x]) + int(string[x:]) not in primes:
			return False
	return True
	
primes = sieve(10000000)
num = int(input())
while num != 0:
	print(str(num) + (' MAGNANIMOUS' if mag(num,primes) else ' PETTY'))
	num = int(input())