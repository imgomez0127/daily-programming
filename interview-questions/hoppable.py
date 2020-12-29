#!/usr/bin/env python3

class Solution:
    def solve(self, nums):
        if not nums:
            return None
        solvable = [False] * len(nums)
        exited = False
        for i, num in enumerate(nums):
            exited |= num >= len(nums)-i-1
            solvable[i] = exited
        last_true = len(nums)-1
        for i in reversed(range(len(nums))):
            solvable[i] |= i+nums[i] >= last_true
            last_true = i if solvable[i] else last_true
        return solvable[0]
