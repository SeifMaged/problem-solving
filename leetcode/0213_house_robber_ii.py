# O(n) Time
# O(1) Space
# Dynamic Programming
from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_robber(nums, left, right):
            rob, skip = 0, 0

            for i in range(left, right):
                rob, skip = skip + nums[i], max(skip,rob)
            
            return max(rob, skip)
        
        return max(house_robber(nums, 0, len(nums)-1), house_robber(nums, 1, len(nums)))
        