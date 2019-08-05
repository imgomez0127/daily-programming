def two_sum(list,k):
    seen_values = set()
    for num in list:
        if k-num in list:
            return True
        seen_values.add(num)
    return False
print(two_sum([4,7,1,-3,2], 5))

