# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Medium
# O(m*n) time, O(m*n) space, where m and n are the number of rows and columns in the grid, respectively
# Breadth First Search
# We can use breadth first search (BFS) to explore the grid level by level. We will start from all the rotten oranges and explore their neighbors. For each rotten orange, we will rot its adjacent fresh oranges and add them to the queue for the next level of BFS. We will keep track of the number of minutes that have passed and the number of fresh oranges remaining. If we rot all fresh oranges, we return the number of minutes. If there are still fresh oranges left after we have processed all rotten oranges, we return -1.
# The time complexity is O(m*n) because in the worst case we may need to visit every cell in the grid, and the space complexity is O(m*n) because we may need to store all cells in the queue for BFS.

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Initialize
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
