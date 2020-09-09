#!/usr/bin/env python3
"""
   Name    : leetcode53.py
   Author  : Ian Gomez
   Date    : September 8, 2020
   Description : Maximum Subarry solved in O(n)
   Github  : imgomez0127@github
"""
from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for val in nums:
            cur_sum = max(val, cur_sum+val)
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
