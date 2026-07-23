# O(n) Time
# O(n) Space

# Hashsets

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numberSet = set(nums)

        for num in numberSet:
            if num-1 not in numberSet:
                current = 1
                while num+1 in numberSet:
                    current += 1
                    num += 1
                
                longest = max(longest, current)
        
        return longest