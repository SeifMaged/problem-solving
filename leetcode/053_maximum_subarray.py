# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Medium
# O(n) time, O(1) space
# Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum