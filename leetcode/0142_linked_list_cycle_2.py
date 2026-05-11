# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
# Medium
# O(n) time, O(1) space, where n is the number of nodes in the linked list.
# Linked List, Two Pointers, Slow and Fast Pointers, Floyd's Tortoise and Hare Algorithm
# We use two pointers, slow and fast, to traverse the linked list. The slow pointer
# moves one step at a time, while the fast pointer moves two steps at a time. If there 
# is a cycle in the linked list, the fast pointer will eventually meet the slow pointer
# in O(n) time. Once they meet, we reset one of the pointers to the head of the linked list 
# and keep the other pointer at the meeting point. We then move both pointers one step at a 
# time until they meet again. The point at which they meet will be the start of the cycle.

# This works because when the two pointers meet, the distance from the head to the start of the 
# cycle is equal to the distance from the meeting point to the start of the cycle. 
# Therefore, when we reset one pointer to the head and keep the other at the meeting point, 
# they will both be at the same distance from the start of the cycle, and moving them one step at a 
# time will lead them to meet at the start of the cycle. If there is no cycle, the fast pointer will 
# reach the end of the linked list and we will return None.

# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None