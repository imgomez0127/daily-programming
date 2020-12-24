#!/usr/bin/env python3

#https://www.hackerrank.com/challenges/maximum-palindromes/problem

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
S = ""
def initialize(s):
    # This function is called once before all queries.
    global S
    S = s

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
def comb(n, r):
    ans = ((math.factorial(n)%1000000007)/(math.factorial(r)*math.factorial(n-r)))
    return int(ans % 1000000007)

def answerQuery(l, r):
    s = S[l-1:r]
    letter_counts = Counter(s)
    pairs = 0
    for char, value in letter_counts.items():
        letter_counts[char] -= (value // 2) * 2
        if (value // 2) > 0:
            pairs += (value//2)
    middles = 0
    for value in letter_counts.values():
        print(letter_counts)
        middles += value
    if middles == 0:
        middles = 1
    total = comb(pairs, pairs-1) * middles
    return total % 1000000007
    # Return the answer for this query modulo 1000000007.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
