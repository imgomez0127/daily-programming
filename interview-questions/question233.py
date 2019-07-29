"""
    Implement O(1) space Fib function
"""
def fib(n):
    a = 0
    b = 1
    for _ in range(n-1):
        b = a + b
        a = b - a
    return a
if __name__ == "__main__":
    print(fib(1))
