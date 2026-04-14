# O(n+m) Time, where n is the length of list1 and m is the length of list2
# O(1) Space

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        merged_trav = dummy
        trav1 = list1
        trav2 = list2

        while trav1 and trav2:
            if trav1.val < trav2.val:
                merged_trav.next = trav1
                trav1 = trav1.next
            else:
                merged_trav.next = trav2
                trav2 = trav2.next
            
            merged_trav = merged_trav.next
        
        if trav1:
            merged_trav.next = trav1
        else:
            merged_trav.next = trav2
        
        return dummy.next
