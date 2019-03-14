from time import time
def timing(f):
    def func(*args, **kwargs):
        before = time()
        rv = f(*args, **kwargs)
        after = time()
        print("elapsed time ", after-before)
        return rv
    return func
def ntimes(n):
    def wrapper(f):
        def fun(*args,**kwargs):
            counter = 0
            for _ in range(n):
                rv = f(*args,**kwargs)
            return rv
        return fun
    return wrapper
@timing
@ntimes(100000000)
def add(x,y=10):
    return x + y
print("add(5,10)",add(5))
