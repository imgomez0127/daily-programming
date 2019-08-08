import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        top_down_view = np.max(grid,axis=0)
        left_right_view = np.max(grid,axis=1)
        grid_arr = np.asarray(grid)
        height_difference = top_down_view - grid_arr
        height_difference2 = (left_right_view - grid_arr.T).T
        total_difference = np.minimum(height_difference,height_difference2)
        total_difference[total_difference < 0] = 0
        return np.sum(total_difference.reshape(-1))
print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
