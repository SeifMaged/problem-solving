# leetcode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Medium
# O(nlogk) time, O(n) space

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        max_heap = []
        for key, value in freqs.items():
            heapq.heappush(max_heap, (-value, key))

        sol = []
        for i in range(k):
            _, key = heapq.heappop(max_heap)
            sol.append(key)
        
        return sol