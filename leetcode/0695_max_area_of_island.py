# 695. Max Area of Island
# leetcode.com/problems/max-area-of-island/
# Medium
# O(m*n) time, O(m*n) space, where m and n are the number of rows and columns in the grid, respectively
# Breadth First Search, Depth First Search
# We can use either breadth first search (BFS) or depth first search (DFS) to explore the grid. We will iterate through each cell in the grid, and when we encounter a '1', we will perform a BFS or DFS to calculate the area of the island by counting all connected '1's. We will keep track of the maximum area found during our iterations. The time complexity is O(m*n) because we may need to visit every cell in the grid, and the space complexity is O(m*n) in the worst case when the grid is filled with '1's and we need to store all of them in the visited set.
# We can also modify the grid in-place to mark visited cells, which would reduce the space complexity however it would still be O(m*n) since the stack or queue used for BFS/DFS can grow up to O(m*n) in the worst case.
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        max_island_size = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(r, c):
            queue = deque()
            grid[r][c] = 0 # to avoid revisiting
            queue.append((r,c))
            size = 1

            while queue:
                row, col = queue.popleft()
                
                for direction in directions:
                    dest_row, dest_col = row + direction[0], col + direction[1]

                    if (min(dest_row,dest_col) < 0 or dest_row >= rows or dest_col >= cols or grid[dest_row][dest_col] == 0):
                        continue
                    
                    queue.append((dest_row, dest_col))
                    grid[dest_row][dest_col] = 0
                    size += 1
            
            return size
        
        def dfs(r, c):
            grid[r][c] = 0
            stack = []
            stack.append((r,c))
            size = 1

            while stack:
                row, col = stack.pop()
                for direction in directions:
                    dest_row, dest_col = row + direction[0], col + direction[1]

                    if (min(dest_row, dest_col) < 0 or dest_row >= rows or dest_col >= cols or grid[dest_row][dest_col] == 0):
                        continue
                    size += 1
                    stack.append((dest_row, dest_col))
                    grid[dest_row][dest_col] = 0
            
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island_size = max(max_island_size, dfs(r,c))
        
        return max_island_size