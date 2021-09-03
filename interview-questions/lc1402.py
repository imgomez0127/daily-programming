#!/usr/bin/env python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_val = 0
        satisfaction.sort()
        for i in reversed(range(len(satisfaction))):
            sat = [i * val for i, val in enumerate(satisfaction[i:])]
            max_val = max(max_val, sum(sat))
        return max_val

if __name__ == '__main__':
    print(Solution().maxSatisfaction([-1,-8,0,5,-9]))
