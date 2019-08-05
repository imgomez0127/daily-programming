class Solution: 
    def getRange(self, arr, target):
        beginning = -1
        found_first_item = False
        for i,n in enumerate(arr):
            if n == target and not found_first_item:
                beginning = i
                found_first_item = True
            if n != target and found_first_item:
                return beginning,i-1
        return beginning,-1
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
#TODO Bin search implementation for lower algorithmic complexity
