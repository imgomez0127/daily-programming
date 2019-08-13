from functools import reduce
def product(lst):
    return reduce(lambda x,y: x * y, lst)
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if nums == []:
            return []

        if product(nums) < k:
            return [nums] + self.numSubarrayProductLessThanK(nums[1:],k) + self.numSubarrayProductLessThanK(nums[:-1],k)

        return self.numSubarrayProductLessThanK(nums[1:],k) + self.numSubarrayProductLessThanK(nums[:-1],k)

if __name__ == "__main__":
    lst1 = []
    lst2 = [10, 5, 2, 6] 
    lst3 = [10,11,6]
    print(Solution().numSubarrayProductLessThanK(lst1,100))
    print(Solution().numSubarrayProductLessThanK(lst2,100))
    print(Solution().numSubarrayProductLessThanK(lst3,60))
