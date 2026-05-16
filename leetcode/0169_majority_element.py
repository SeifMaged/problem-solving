# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# O(n) time, O(1) space
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = nums[0]
        redundancy = 1

        for i in range(1, len(nums)):
            if element == nums[i]:
                redundancy += 1
            else:
                redundancy -= 1
                if redundancy == 0:
                    element = nums[i]
                    redundancy = 1
            
        return element