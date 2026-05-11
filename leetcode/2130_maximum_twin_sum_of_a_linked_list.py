# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Medium
# O(n) time, O(1) space, where n is the number of nodes in the linked list.
# Linked List, Two Pointers, Slow and Fast Pointers
# We use two pointers, slow and fast, to find the middle of the linked list.
# Once we find the middle, we reverse the second half of the linked list. 
# Then, we use two pointers to traverse both halves of the linked list simultaneously
# and calculate the twin sum for each pair of nodes. We keep track of the maximum twin sum
# and return it at the end. The space complexity is O(1) because we are modifying the linked list
# in place and using only a few pointers and variables.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the 2nd half of the list
        prev = None
        current = slow

        while current: 
            next = current.next
            current.next = prev
            prev = current
            current = next

        max_twin = 0
        fast = prev # Head of the reversed 2nd half
        slow = head

        while fast:
            max_twin = max(max_twin, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
        
        return max_twin