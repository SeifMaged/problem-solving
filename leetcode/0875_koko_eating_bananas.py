# leetcode 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Medium
# O(nlogm) time, O(1) space

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)

        result = right

        while left <= right:
            rate = (left + right) // 2

            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile/rate)
            
            if totalTime <= h:
                result = rate
                right = rate - 1
            else:
                left = rate + 1
        
        return result