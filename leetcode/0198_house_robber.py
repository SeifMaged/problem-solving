# 198. House Robber
# leetcode.com/problems/house-robber/
# Medium
# O(n) time, O(1) space, where n is the number of houses
# Dynamic Programming

# We can use dynamic programming to solve this problem. 

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed_prev, didnt_rob_prev = nums[0], 0

        for i in range(1, len(nums)):
            current_house = nums[i]
            robbed_prev, didnt_rob_prev = max(robbed_prev, didnt_rob_prev + current_house), robbed_prev

        return robbed_prev