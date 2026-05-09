# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Medium
# O(n) time, O(1) space, where n is the length of the height array and the space is O(1) because we are only using a few pointers and variables
# Two Pointers
# We use two pointers, left and right, to keep track of the current position in the height array. We start both pointers at the beginning and end of the array, respectively. We calculate the current water area using the formula min(height[left], height[right]) * (right - left) and update the maximum water area if the current area is greater. We then move the pointer that has the smaller height, since moving the taller pointer will not increase the area.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1

        max_water = 0

        while left < right:
            current_water = min(height[left], height[right]) * (right-left)
            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water