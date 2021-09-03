import math
import os
import random
import re
import sys
import collections

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    anagrams = collections.Counter()
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            cnt = frozenset(collections.Counter(s[i:j+1]).items())
            anagrams[cnt] += 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1)// 2
    return count

print(sherlockAndAnagrams('cdcd'))
