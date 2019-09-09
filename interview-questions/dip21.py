def first_missing_positive(nums):
    nums_set = set(nums)
    for i in range(1,max(nums)):
        if i not in nums_set:
            return i
print(first_missing_positive([3, 4, -1, 1]))
# 2
