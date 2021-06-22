#!/usr/bin/env python3.9

import collections
import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        cur_bribes = 0
        cur_val = q[i]
        # Exit as early as possible
        if q[i]-i-1 > 2:
            print("Too chaotic")
        # Check if anything behind is greater than cur val
        for j in range(max(0, q[i]-2), i):
            if q[j] < cur_val:
                bribes += 1
    print(bribes)



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
