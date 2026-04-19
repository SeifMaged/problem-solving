# Medium
# Binary Search
# O(log(m) + log(n)) Time, where m is the number of rows and n is the number of columns in the matrix.
# O(1) Space
# We can treat the 2D matrix as a 1D sorted array and perform binary search to find the target. First, we perform a binary search to find the correct row where the target may exist, and then we perform another binary search within that row to find the target.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        low, high = 0, ROWS-1

        while low <= high:
            row = (low + high)//2

            if matrix[row][-1] < target:
                low = row + 1
            elif matrix[row][0] > target:
                high = row - 1
            else:
                break
        
        if high < low:
            return False
        
        row = (low + high) // 2

        left, right = 0, COLS-1

        while left <= right:
            middle = (left + right)//2
            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                return True
        
        return False

