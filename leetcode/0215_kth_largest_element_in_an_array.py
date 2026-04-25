# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Medium
# O(n log k) time, O(k) space, where n is the number of
# elements in the input array and k is the value of k in the problem
# Heap, Priority Queue
# We maintain a min-heap of size k to keep track of the k largest elements in the array. When we add a new element, we compare it to the smallest element in the heap (the root). If the new element is larger, we replace the root with the new element and heapify. This way, the root of the heap always contains the kth largest element.
# The time complexity for adding an element is O(log k) because we may need to heapify the heap after adding a new element. The space complexity is O(k) because we are maintaining a heap of size k.
# This problem can also be solved using the Quickselect algorithm with an average time complexity of O(n) and worst-case time complexity of O(n^2), but the heap approach is more straightforward and easier to implement.

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [] 

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return heapq.heappop(min_heap)
