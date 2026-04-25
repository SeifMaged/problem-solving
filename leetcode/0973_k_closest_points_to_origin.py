# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Medium
# O(n log k) time, O(k) space, where n is the number of points and k is the number of closest points to return
# Heap
# The reason for O(n log k) time complexity is that we iterate through all n points and perform a heap push operation which takes O(log k) time. The space complexity is O(k) because we maintain a heap of size k to store the closest points.
# This problem can also be solved using the Quickselect algorithm with an average time complexity of O(n) and worst-case time complexity of O(n^2), but the heap approach is more straightforward and easier to implement.

import heapq

from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for point in points:
            x, y = point[0], point[1]
            distance = x**2 + y**2
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        return [point for _, point in heap]