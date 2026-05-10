# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Hard
# O(n) time, O(1) space, where n is the length of the height array and the space is O(1) because we are only using a few pointers and variables
# Two Pointers

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        max_left, max_right = height[0], height[-1]
        total = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                total += max_left - height[left]
            
            else:
                right -= 1
                max_right = max(max_right, height[right])
                total += max_right - height[right]

        return total