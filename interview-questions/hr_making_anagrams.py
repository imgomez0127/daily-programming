#!/usr/bin/env python3

def makeAnagram(a, b):
    a_cnt = collections.Counter(a)
    for c in b:
        a_cnt[c] -= 1
    return sum(map(abs, a_cnt.values()))
