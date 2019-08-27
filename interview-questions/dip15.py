class Solution:
    def find_first_zero(self,nums):
        for i,num in enumerate(nums):
            if num == 0:
                return i
        return -1

    def moveZeros(self, nums):
        # Fill this in.
        first_zero = self.find_first_zero(nums)
        cursor = first_zero
        for i in range(first_zero,len(nums)):
            if nums[i] != 0:
                nums[i],nums[cursor] = nums[cursor],nums[i]
                cursor += 1

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
nums2 = [3,0,2,0]
Solution().moveZeros(nums)
Solution().moveZeros(nums2)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
print(nums)
print(nums2)
