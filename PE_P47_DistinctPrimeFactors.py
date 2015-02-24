## Author: James Norcross
## Date: 2/23/15
## Description:

from math import sqrt

## a prime sieve function
def makePrimeSieve(max):
    sieve = []
    
    ## initialize to true
    for i in range(max):
        sieve.append(True)
        
    ## make sieve
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True
    
    imax = int(sqrt(max)) + 1
    
    for i in range(2,imax):
        if(sieve[i]):
            for j in range(2*i, max, i):
                sieve[j] = False

    return sieve

## creates a list from sieve
def listFromSieve(sieve):
    
    myList = []
    
    for i in range(0, len(sieve)):
        if (sieve[i]):
            myList.append(i)

    return myList

## determines whether number has n distinct prime factors
def hasNDistinctPrimeFactors(primes, n, number):
    
    factorCount = 0
    primeIndex = 0
    
    while(primes[primeIndex] < number):
        if(number % primes[primeIndex] == 0):
            factorCount += 1
            if(factorCount > n):
                return False
        primeIndex += 1
        
    if(factorCount == n):
        return True
    
    else:
        return False

max = 1000000
sieve = makePrimeSieve(max)
primes = listFromSieve(sieve)
consecutive = 0
initial = 0

for i in range(1000000):
    if(hasNDistinctPrimeFactors(primes, 4, i)):
        consecutive += 1
        if(consecutive == 1):
            initial = i
        if(consecutive == 4):
            print initial
            break
    else:
        consecutive = 0;

print "done"
            
            
            
