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
        for val in candidates:
            if val <= target:
                results = self.find_combinations(candidates, target-val)
                for arr in results:
                    arr.append(val)
                combinations.extend(results)
            else:
                combinations.extend(self.find_combinations(candidates[1:], target))
        return combinations

    def filter(self, combinations):
        final = set()
        for combination in combinations:
            final.add(tuple(sorted(combination)))
        return list(map(lambda x: list(x), final))

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = self.find_combinations(candidates, target)
        results = self.filter(results)
        return results


if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7], 6))
