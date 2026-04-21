# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# Medium
# O(n) time, O(1) space
# Counting Sort

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0]*3

        for num in nums:
            colors[num] += 1
        
        i = 0
        for color in range(len(colors)):
            for j in range(colors[color]):
                nums[i] = color
                i += 1
        