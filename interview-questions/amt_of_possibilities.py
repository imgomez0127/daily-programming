def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def amt_of_possibilities_helper(x,y):
    if x == 0 and y == 0:
        return 1
    if x == 0:
        return amt_of_possibilities_helper(x,y-1)
    if y == 0: 
        return amt_of_possibilities_helper(x-1,y)
    go_right = amt_of_possibilities_helper(x-1,y)
    go_down = amt_of_possibilities_helper(x,y-1)
    return go_down + go_right

def amt_of_possibilities(n):
    return amt_of_possibilities_helper(n-1,n-1)
print(amt_of_possibilities(5))

#1 1 1 1 1
#1 1 1 1 1
#1 1 1 1 1
#1 1 1 1 1
#1 1 1 1 1
