# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Medium
# O(n) time, O(1) space, where n is the length of the nums array and the space is O(1) because we are using the result array to store the products and only a few variables for prefix and postfix products
# Prefix Sum

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]        
        return result