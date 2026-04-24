# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Easy
# O(log k) time, O(k) space, where k is the value of k in the problem
# Heap, Priority Queue
# We maintain a min-heap of size k to keep track of the k largest elements in the stream. When we add a new element, we compare it to the smallest element in the heap (the root). If the new element is larger, we replace the root with the new element and heapify. This way, the root of the heap always contains the kth largest element.
# The time complexity for adding an element is O(log k) because we may need to heapify the heap after adding a new element. The space complexity is O(k) because we are maintaining a heap of size k.

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        
        heapq.heapify(self.stream)

        while len(self.stream) > self.k:
            heapq.heappop(nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        
        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)