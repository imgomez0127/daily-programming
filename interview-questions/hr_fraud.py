#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    counting_arr = [0 for _ in range(max(expenditure)+1)]
    alert_count = 0
    for val in expenditure[:d]:
        counting_arr[val] += 1
    for i, val in enumerate(expenditure[d:]):
        median_arr = []
        for j, count in enumerate(counting_arr):
            median_arr.extend([j for _ in range(count)])
        if d%2 == 0:
            middle1 = d//2
            middle2 = (d//2)-1
            median = (median_arr[middle1] + median_arr[middle2])/2
        else:
            middle = d//2
            median = median_arr[middle]
        if val >= 2*median:
            alert_count += 1
        counting_arr[expenditure[i]] -= 1
        counting_arr[val] += 1
    return alert_count

exp = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 4
print(activityNotifications(exp, 5))
