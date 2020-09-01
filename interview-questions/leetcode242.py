#!/usr/bin/env python3
#
from collections import Counter

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        count_same = True
        for val in s_count.keys():
            count_same &= s_count[val] == t_count[val]
        return len(s_count.keys()) == len(t_count.keys()) and count_same

class Solution2:

    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter()
        for c1,c2 in zip(s,t):
            d[c1] += 1
            d[c2] += 1
        return len(s) == len(t) and all(val == 0 for val in d.values())

print(Solution().isAnagram("nagaram","anagram"))
