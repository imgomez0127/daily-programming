#!/usr/bin/env python3

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter(s[0])
        max_len = 1
        i = 0
        j = 1
        while j != len(s):
            if count[s[j]] >= 1:
                count[s[i]] -= 1
                i += 1
            else:
                count[s[j]] += 1
                max_len = max(max_len, (j+1)-i)
                j += 1
        return max_len

if __name__ == "__main__":
    S1 = "abcabcbb"
    S2 = "bbbbb"
    S3 = "pwwkew"
    print(Solution().lengthOfLongestSubstring(S1))
    print(Solution().lengthOfLongestSubstring(S2))
    print(Solution().lengthOfLongestSubstring(S3))
