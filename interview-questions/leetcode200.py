#!/usr/bin/env python3
from queue import Queue

class Solution:

    def __init__(self):
        self.q = Queue()
        self.seen = set()
        self.count = 0

    def numIslands_helper(self, grid):
        while not self.q.empty():
            i, j = self.q.get()
            if grid[i][j] == "1" and (i,j) not in self.seen:
                self.q.put((max(0, i-1), j))
                self.q.put((i, max(0, j-1)))
                self.q.put((min(len(grid)-1, i+1), j))
                self.q.put((i, min(len(grid[i])-1, j+1)))
            self.seen.add((i, j))

    def numIslands(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in self.seen and grid[i][j] == '1':
                    self.q.put((i, j))
                    self.numIslands_helper(grid)
                    self.count += 1
        return self.count

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))
print(Solution().numIslands(grid2))
