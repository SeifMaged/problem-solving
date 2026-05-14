# 2784. Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/
# Easy
# O(n log n) time, O(1) space, where n is the length of the nums array and the space is O(1) because we are sorting the array in place
# Sorting
# Daily Problem - 14/5/2026

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        nums = sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] != i+1:
                return False
        
        return nums[-1] == nums[-2]