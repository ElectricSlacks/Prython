import math 

def simpleSieve(sieveSize):
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in xrange(i**2, sieveSize+1, i):
            sieve[pointer] = False
    # Sieve is left with prime numbers == True
    primes = []
    for i in xrange(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes

sieveSize = input()
primes = simpleSieve(sieveSize)

f = open('Primes.txt', 'w')
f= write('Primes.txt , 'primes')
