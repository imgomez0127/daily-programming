#!/usr/bin/env python3
"""
   Name    : leetcode238.py
   Author  : Ian Gomez
   Date    : September 7, 2020
   Description : Product of Array Except Self
   Github  : imgomez0127@github
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #need left and right pass
        left = []
        right = []
        cur1 = cur2 = 1
        for i, (val1, val2) in enumerate(zip(nums,reversed(nums))):
            left.append(cur1)
            right.append(cur2)
            cur1 *= val1
            cur2 *= val2
        right.reverse()
        return [left[i] * right[i] for i in range(len(nums))]

if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
