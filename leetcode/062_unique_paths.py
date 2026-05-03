# 62. Unique Paths
# leetcode.com/problems/unique-paths/
# Medium
# O(m*n) time, O(m) space, where n is the number of rows and m is the number of columns
# Dynamic Programming - Bottom Up

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev_row = [0] * m

        for i in range(n-1, -1, -1):
            current_row = [0] * m
            current_row[m-1] = 1

            for j in range(m-2, -1, -1):
                current_row[j] = current_row[j+1] + prev_row[j]
            
            prev_row = current_row
        
        return current_row[0]
