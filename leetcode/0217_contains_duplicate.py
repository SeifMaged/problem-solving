# Easy
# Hash Table / Set
# O(n) Time, where n is the length of nums
# O(n) Space, where n is the length of nums

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False