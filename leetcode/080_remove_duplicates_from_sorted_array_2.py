# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Medium
# O(n) time, O(1) space, where n is the length of the array and the space is O(1) because we are modifying the array in place and using only a few pointers and variables
# Two Pointers
# We use two pointers, left and right, to keep track of the current position in the array. We start both pointers at index 2, since the first two elements can always be kept. We iterate through the array with the right pointer, and if the current element is not equal to the element at left-2, it means we can keep this element and move it to the left pointer's position. We then increment the left pointer. Finally, we return the left pointer as the new length of the array without duplicates.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2

        for right in range(2, len(nums)):
            if nums[right] != nums[left-2]:
                nums[left] = nums[right]
                left += 1
        
        return left
        