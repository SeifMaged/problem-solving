# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Medium
# O(n) time, O(1) space
# Kadane's Algorithm

# Main idea: The maximum sum of a circular subarray can be found by either:
# 1. Finding the maximum sum of a non-circular subarray using Kadane's
# 2. Finding the minimum sum of a non-circular subarray and subtracting it from the total sum of the array. 
# This works because the maximum circular subarray can be thought of as the total sum minus the minimum subarray.

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_max = 0

        min_sum = float('inf')
        current_min = 0

        total = 0 

        for i in range(len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            max_sum = max(max_sum, current_max)

            current_min = min(current_min + nums[i], nums[i])
            min_sum = min(min_sum, current_min)

            total += nums[i]
        
        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total - min_sum)