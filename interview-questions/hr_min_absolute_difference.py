#!/usr/bin/env python3

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float('inf')
    op1 = arr[0]
    for op2 in arr[1:]:
        min_diff = min(min_diff, abs(op1-op2))
        op1 = op2
    return min_diff
