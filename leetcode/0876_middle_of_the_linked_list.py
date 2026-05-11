# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Easy
# O(n) time, O(1) space, where n is the number of nodes in the linked list and the space is O(1) because we are only using a few pointers and variables
# Linked List, Two Pointers, Slow and Fast Pointers
# We use two pointers, slow and fast, to traverse the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
# When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle node. If there are two middle nodes, we return the second middle 
# node, which is what the problem asks for.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow