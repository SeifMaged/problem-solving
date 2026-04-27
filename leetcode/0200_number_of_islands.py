# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Medium
# O(m*n) time, O(m*n) space, where m and n are the
# number of rows and columns in the grid, respectively
# Breadth First Search, Depth First Search
# We can use either breadth first search (BFS) or depth 
# first search (DFS) to explore the grid. We will iterate
# through each cell in the grid, and when we encounter a '1',
# we will perform a BFS or DFS to mark all connected '1's as
# visited. This way, we can count the number of islands by
# counting how many times we perform a BFS or DFS. The time
# complexity is O(m*n) because we may need to visit every
# cell in the grid, and the space complexity is O(m*n)
# in the worst case when the grid is filled with '1's and
# we need to store all of them in the visited set.

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0

        directions = ((1,0), (-1, 0), (0, 1), (0, -1))
        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                for dir_r, dir_c in directions:
                    r, c = row + dir_r, col + dir_c
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands