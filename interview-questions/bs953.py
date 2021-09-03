#!/usr/bin/env python3
import collections

class Solution:
    def solve(self, s, t):
        cnt1 = collections.Counter()
        cnt2 = collections.Counter()
        for c1, c2 in zip(s, t):
            if c1 != c2:
                cnt1[c1] += 1
                cnt2[c2] += 1
        max_value = min(2, len(set_1.intersection(set_2)))
        return len(set_1) - max_value
