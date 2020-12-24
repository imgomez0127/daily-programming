#!/usr/bin/env python3
from collections import Counter

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        alpha_len = 26
        change_counts = Counter()
        for c1, c2 in zip(s, t):
            change_counts[(ord(c2)-ord(c1))%alpha_len] += 1
        del change_counts[0]
        for val, amt in change_counts.items():
            for i in range(amt):
                print(val + 26 * i)
                if val + 26 * i > k:
                    return False
        return len(s) == len(t)

if __name__ == "__main__":
    print(Solution().canConvertString("input", "ouput", 9))
    print(Solution().canConvertString("abc", "bcd", 10))
    print(Solution().canConvertString("aab", "bbb", 27))
    print(Solution().canConvertString("atmtxzjkz", "tvbtjhvjd", 35))
