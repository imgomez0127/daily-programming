def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    def fib2_helper(n,a,b):
        if n == 0:
            return a
        return fib2_helper(n-1,b,a+b)
    return fib2_helper(n,0,1)

def fib3(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        b = a + b
        a = b - a
    return a
if __name__ == "__main__":
    print(fib1(3))
    print(fib2(3))
    print(fib3(3))
