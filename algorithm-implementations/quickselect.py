#!/usr/bin/env python3
import random
def hoare_partition(nums):
    i = 0
    j = len(nums)-1
    pivot_ind = random.randrange(len(nums))
    pivot = nums[pivot_ind]
    while True:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]
    pivot_ind = hoare_partition(nums)
    print(nums, pivot_ind, k)
    if pivot_ind == len(nums)-k:
        return nums[pivot_ind]
    if len(nums)-k > pivot_ind:
        return quickselect(nums[pivot_ind+1:], k)
    return quickselect(nums[:pivot_ind], k-pivot_ind)

x = [0,5,3,2,1,4]
print(quickselect([0,5,1,2,3,4], 2))
