import math 
file = open('Primes.txt', 'w')
file.close()

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
str(primes) = simpleSieve(sieveSize)

file = open("Primes.txt","w")
file.write(Primes)
file.close()
