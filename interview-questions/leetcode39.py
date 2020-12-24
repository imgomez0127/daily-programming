#!/usr/bin/env python3
"""
   Name    : leetcode39.py
   Author  : Ian Gomez
   Date    : October 9, 2020
   Description :
   Github  : imgomez0127@github
"""
from typing import List

class Solution:
    def find_combinations(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        if candidates == [] or target < 0:
            return combinations
        if target == 0:
            return [[]]
        for i, val in enumerate(candidates):
            if val <= target:
                results = self.find_combinations(candidates, target-val)
                for arr in results:
                    arr.append(val)
                combinations.extend(results)
            else:
                combinations.extend(self.find_combinations(candidates[i+1:], target))
        return combinations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = self.find_combinations(candidates, target)
        return results


if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7], 7))
