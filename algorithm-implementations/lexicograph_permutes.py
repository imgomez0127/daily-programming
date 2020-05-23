from copy import copy
def has_increasing_order(s):
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            return True
    return False

def find_low_index(s):
    low_index = 0
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            low_index = i 
    return low_index
def find_high_index(s,low_index):
    high_index = low_index+1
    for i in range(low_index+1,len(s)):
        if s[low_index] < s[i]:
            high_index = i
    return high_index
def lexicographicPermutes(s):
    s = list(sorted(s))
    all_permutes = ["".join(s)]
    while has_increasing_order(s):
        s = copy(s)
        low_index = find_low_index(s)
        high_index = find_high_index(s,low_index) 
        s[low_index],s[high_index] = s[high_index],s[low_index]
        new_permute = s[:low_index+1]+list(reversed(s[low_index+1:]))
        all_permutes.append("".join(new_permute))
        s = new_permute
    return all_permutes

print(lexicographicPermutes(["1","2","3","4","5","6","7","8","9"]))
