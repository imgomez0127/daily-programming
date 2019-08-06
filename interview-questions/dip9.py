def singleNumber(nums):
    xor_accumulator = 0
    for num in nums:
        xor_accumulator ^= num
    return xor_accumulator

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

