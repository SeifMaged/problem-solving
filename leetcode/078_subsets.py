# 78. Subsets
# https://leetcode.com/problems/subsets/
# Medium
# O(n * 2^n) time, O(n) space, where n is the length of the input array
# Backtracking, Depth First Search
# We have 2^n subsets for an array of length n, and we spend O(n) time to copy each subset to the output list. The space complexity is O(n) because of the recursion stack and the temporary subset list.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        subset = []
        def dfs(index):
            if index >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(index+1)

            subset.pop()
            dfs(index+1)
        
        dfs(0)

        return output