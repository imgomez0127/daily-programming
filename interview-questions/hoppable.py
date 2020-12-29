#!/usr/bin/env python3

class Solution:
    def solve(self, nums):
        if not nums:
            return None
        reach = 0
        for i, n in enumerate(nums):
            if i > reach:
                return False
        return True
