# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Medium
# O(n) time, O(1) space
# Sliding Window

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        left = 0
        min_length = float('inf')

        for right in range(len(nums)):
            running_sum += nums[right]

            while running_sum >= target:
                min_length = min(min_length, right-left+1)
                running_sum -= nums[left]
                left += 1
            
        return min_length if min_length != float('inf') else 0