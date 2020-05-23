import time
class PrimeSieve:
    def __init__(self,limit):
        self.__is_prime = []
        self.__limit = limit
        self.__num_primes = 0
        self.__max_prime = 2
        self.sieve()

    def sieve(self):
        self.__is_prime.append(False)
        self.__is_prime.append(False)
        for _ in range(2,self.__limit+1):
            self.__is_prime.append(True)
        for i in range(2,int((self.__limit)**(1/2))+1):
            if self.__is_prime[i]:
                for j in range(i**2,self.__limit+1,i):
                    self.__is_prime[j] = False


if __name__ == '__main__':
        a = PrimeSieve(100000000)
