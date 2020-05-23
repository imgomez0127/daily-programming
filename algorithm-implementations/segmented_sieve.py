import math

def sieve(a, b):
    is_prime = [not (i in (0, 1)) for i in range(int(b**0.5)+1)]
    high_primes = [True for _ in range(b-a+1)]
    for i in range(int(b**0.25)+1):
        if is_prime[i]:
            for j in range(i**2,int(b**0.5)+1,i):
                is_prime[j] = False
    low_primes = [i for i,primality in enumerate(is_prime) if primality]
    for p in low_primes:
        i = math.ceil(a/p)*p-a
        if a <= p:
            i = i + p
        for j in range(i,len(high_primes),p):
            high_primes[j] = False
    for i,prime in enumerate(high_primes):
        if prime and (i + a) != 1:
            print(i+a)
    print()

if __name__ == "__main__":
    a=input()

    for i in range(int(a)):
        case=input()
        primes=case.split(" ")
        sieve(int(primes[0]),int(primes[1]))
