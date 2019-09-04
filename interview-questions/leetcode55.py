class Solution:
    def canJumpHelper(self,nums,position,able_to_reach_end):
        if able_to_reach_end[position] != 0:
            return True if able_to_reach_end[position] == 1 else False
        else:
            if position >= len(nums)-1:
                return True
            for jump_amount in range(1,nums[position]+1):
                if self.canJumpHelper(nums,position+jump_amount,able_to_reach_end):
                    able_to_reach_end[position] = 1
                    return True
            able_to_reach_end[position] = -1
            return False

    def canJump(self, nums):
        able_to_reach_end = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return True
        for jump_amount in range(1,nums[0]+1):
            if self.canJumpHelper(nums,jump_amount,able_to_reach_end):
                return True
        return False

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))

