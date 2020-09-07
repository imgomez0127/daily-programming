#!/usr/bin/env python3
"""
   Name    : leetcode238.py
   Author  : Ian Gomez
   Date    : September 7, 2020
   Description :
   Github  : imgomez0127@github
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #need left and right pass
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]
        out = [0 for _ in range(len(nums))]
        cur1 = cur2 = 1
        cur2 = 1
        for i in range(len(nums)):
            left[i] = cur1
            right[i] = cur2
            cur1 *= nums[i]
            cur2 *= nums[len(nums)-i-1]
        right.reverse()
        for i in range(len(nums)):
            out[i] = left[i] * right[i]
        return out

if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
