# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Medium
# O(n^m) time, O(m) space, where n is the length of the input array and m is the target value
# Backtracking, Depth First Search
# We have n choices for each of the m positions in the combination, leading to O(n^m) time complexity. The space complexity is O(m) because of the recursion stack and the temporary combination list.

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, current, total):
            if total == target:
                output.append(current.copy())
                return
            if i >= len(nums) or total > target:
                return 
            
            current.append(nums[i])
            dfs(i, current, total + nums[i])

            current.pop()
            dfs(i+1, current, total)
        
        dfs(0, [], 0)
        return output