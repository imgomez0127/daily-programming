"""
    Asked by palantir compute the next lexicographic permutation 
    (as a challenge do it without allocating extra memory)
"""
def swap(i,j,arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def findNextPerm(arr):
    
