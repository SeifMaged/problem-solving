# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Easy
# O(n) time, O(k) space
# Sliding Window

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        window = set()

        for right in range(len(nums)):
            if right-left > k:
                window.remove(nums[left])
                left += 1
            
            if nums[right] in window:
                return True
            
            window.add(nums[right])
        
        return False

