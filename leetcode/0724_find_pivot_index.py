# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Easy
# O(n) time, O(1) space, where n is the length of the nums array and the space is O(1)
# Prefix Sum

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            suffix = total - prefix - nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
        
        return -1