#!/usr/bin/env python3
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head = 0
        tail = len(nums)-1
        new_nums = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if abs(nums[tail]) > abs(nums[head]):
                new_nums[i] = nums[tail] ** 2
                tail -= 1
            else:
                new_nums[i] = nums[head] ** 2
                head += 1
        return new_nums
