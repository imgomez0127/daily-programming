#!/usr/bin/env python3

class Solution:

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left),n-min(right))
