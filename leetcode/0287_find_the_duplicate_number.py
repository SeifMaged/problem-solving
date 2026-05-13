# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Medium
# O(n) time, O(1) space, where n is the length of the nums array
# Floyd's Tortoise and Hare (Cycle Detection)
# We can treat the numbers in the array as pointers to indices, which creates a linked list
# The duplicate number will create a cycle in this linked list. We can use Floyd's Tortoise 
# and Hare algorithm to find the entry point of the cycle, which will be the duplicate number.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        
        return -1