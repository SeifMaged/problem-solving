# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/
# Easy

from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        sol = []

        for num in nums:
            str_representation = str(num)

            for char in str_representation:
                sol.append(int(char))
        
        return sol