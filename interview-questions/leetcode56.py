#!/usr/bin/env python3
"""
   Name    : leetcode56.py
   Author  : Ian Gomez
   Date    : September 7, 2020
   Description :
   Github  : imgomez0127@github
"""
from typing import List
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]
        merged = False
        i = 1
        j = 0
        while i < len(intervals):
            if new_intervals[j][1] >= intervals[i][0]:
                new_intervals[j] = [new_intervals[j][0],max(intervals[i][1],new_intervals[j][1])]
            else:
                new_intervals.append(intervals[i])
                j += 1
            i += 1
        return new_intervals

if __name__ == "__main__":
    pass
