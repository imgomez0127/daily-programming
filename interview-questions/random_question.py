def fun(lst):
    amt_greater = [0 for _ in range(len(lst)+1)]
    max_n_value = len(amt_greater)
    for num in lst:
        if num > max_n_value:
            amt_greater[max_n_value] += 1
        elif num > 0:
            amt_greater[num-1] += 1
    amt_greater_than_n = sum(amt_greater)
    for i in range(len(amt_greater)):
        if i == amt_greater_than_n:
            return i
        amt_greater_than_n -= amt_greater[i]
    return -1

print(fun([1,2,3,4,5]))
print(fun([1,2,3,4]))
print(fun([2,2,4,4,4]))
print(fun([-1,-2,-3,-4]))
print(fun([10,10,10,10,10,10,10,10,10]))
