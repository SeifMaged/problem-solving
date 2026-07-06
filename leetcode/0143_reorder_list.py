from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find half
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        prev = slow.next = None
        
        # slow is at the start of the half
        # Reverse 2nd half of LL
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
