# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Easy
# O(n) time, O(1) space, where n is the number of nodes in the linked list.
# Linked List, Two Pointers, Slow and Fast Pointers
# We use two pointers, slow and fast, to traverse the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer in O(n) time. If there is no cycle, the fast pointer will reach the end of the linked list.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False