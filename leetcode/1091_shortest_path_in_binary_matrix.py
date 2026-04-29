# 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Medium
# O(n^2) time, O(n^2) space, where n is the number of rows (or columns) in the grid
# Breadth First Search
# We can use breadth first search (BFS) to explore the grid level by level.
# We will start from the top-left cell and explore all 8 possible directions 
# (including diagonals) at each step. We will keep track of the path length 
# and mark visited cells to avoid cycles. If we reach the bottom-right cell, 
# we return the path length. If we exhaust all possibilities without reaching 
# the bottom-right cell, we return -1. The time complexity is O(n^2) because in 
# the worst case we may need to visit every cell in the grid, and the space complexity 
# is O(n^2) because we may need to store all cells in the queue for BFS.

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or grid[0][0] == 1:
            return -1
        N = len(grid) # since it is NxN
        if N == 1:
            return 1
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)) # 8 directions

        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1

        path = 1

        while queue:
            path += 1
            for i in range(len(queue)):
                row, col = queue.popleft()

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if min(new_row, new_col) < 0 or max(new_row, new_col) >= N or grid[new_row][new_col] == 1:
                        continue
                    if new_row + 1 == new_col + 1 == N:
                        return path
                    
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col))
        
        return -1
                    