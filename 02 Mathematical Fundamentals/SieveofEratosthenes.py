from math import *


def SieveofEratosthenes(n):
    prime = [True] * (n+1)
    p = prime[0] = prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(sqrt(n))+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime


t = int(input("Please enter a number how many input you give : "))
for i in range(t):
    n = int(input("Please enter a number for prime search : "))
    sieve = SieveofEratosthenes(n)
    for j in range(n+1):
        if sieve[j]:
            print(j, end=" ")
    print()

# Output: Please enter a number how many input you give : 3
