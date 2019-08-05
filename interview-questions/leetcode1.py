class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_numbers = {}
        for i in range(len(nums)):
            if target - nums[i]  in seen_numbers:
                return [seen-target[target-nums[i]],i]
            thingy[nums[i]] = i
        return [-1,-1]

