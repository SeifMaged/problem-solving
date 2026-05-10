# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/
# Easy
# O(n) time, O(n) space, where n is the length of the nums for initialization and O(1) time for sumRange queries, and the space is O(1) because we are storing the prefix sums in an array
# Prefix Sum

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums

        for i in range(1, len(nums)):
            self.prefix[i] += self.prefix[i-1] 
        

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix[left-1] if left != 0 else 0
        return self.prefix[right] - left_sum 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)