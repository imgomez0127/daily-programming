#!/usr/bin/env python3
"""
   Name    : leetcode15.py
   Author  : Ian Gomez
   Date    : September 8, 2020
   Description : Three sum
   Github  : imgomez0127@github
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        seen = set()
        for i in range(1, len(nums)-1):
            seen.add(nums[i-1])
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in x:
                    ans.add((nums[i], nums[j], -(nums[i]+nums[j])))
        return ans

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
