#!/usr/bin/env python3
#
def alternatingCharacters(s):
    adj_chars = [s[0]]
    deleted_amt = 0
    for c in s[1:]:
        if adj_chars[-1] == c:
            deleted_amt += 1
        else:
            adj_chars.append(c)
    return deleted_amt
