#!/usr/bin/env python3
from typing import List
import numpy as np

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        grid = np.asarray(grid)
        positions = [[(i,j) for j in range(len(grid[i]))] for i in range(len(grid))]
        ans = set()
        print(positions)
        for row, position in zip(grid, positions):
            if sum(row) > 1:
                ans.update(list(position))
        print(ans)
        for col, position in zip(grid.T):
            if sum(col) > 1:
                ans.update(list(position))
        return len(ans)

print(Solution().countServers([[1,0],[0,1]]))
print(Solution().countServers([[1,0],[1,1]]))
