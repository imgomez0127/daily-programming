class Solution:
    def canJumpHelper(self,nums,position):
        if position >= len(nums)-1:
            return True
        for jump_amount in range(1,nums[position]+1):
            if self.canJumpHelper(nums,position+jump_amount):
                return True
        return False

    def canJump(self, nums):
        if len(nums) == 1:
            return True
        for jump_amount in range(1,nums[0]+1):
            if self.canJumpHelper(nums,jump_amount):
                return True
        return False

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))

