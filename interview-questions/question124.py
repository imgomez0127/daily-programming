"""
    This question was asked by Microsoft
"""
def fun(n):
    i = n
    rounds = 0
    while(n > 1):
        rounds += 1
        i = int(i/2)
    return rounds
