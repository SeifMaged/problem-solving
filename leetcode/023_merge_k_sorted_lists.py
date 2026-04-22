# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Hard
# O(nk) time, O(1) space
# Greedy, Linked List, Merge

# Possible Improvements:
# Use a min-heap to optimize the time complexity to O(n log k)

from typing import List, Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        valid_lists = set()

        for i in range(len(lists)):
            if lists[i]: # Nonempty linked list
                valid_lists.add(i)
        
        trav = dummy
        
        while valid_lists:
            min_value, min_index = float('inf'), -1
            for i in valid_lists:
                if lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            
            min_node = lists[min_index]
            trav.next = min_node
            trav = trav.next
            
            lists[min_index] = min_node.next
            if lists[min_index] is None:
                valid_lists.remove(min_index)
        
        return dummy.next
