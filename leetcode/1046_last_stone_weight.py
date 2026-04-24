# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
# Easy
# O(n log n) time, O(n) space, where n is the number of stones
# Heap, Greedy
# We can use a max heap to always get the two heaviest stones. We pop the
# two heaviest stones, smash them together, and if they are not of equal weight, we push the difference back into the heap. We repeat this process until there is at most one stone left in the heap. The time complexity is O(n log n) because we need to build the heap and perform heap operations for each stone. The space complexity is O(n) because we need to store all the stones in the heap.
# The reason it is O(n log n) and not O(n^2) is that we are using a heap data structure, which allows us to efficiently retrieve and update the heaviest stones in logarithmic time. If we were to sort the stones after each smash, it would lead to O(n^2) time complexity, but using a heap avoids the need for repeated sorting.

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones] # To simulate max heap
        heapq.heapify(stones) # O(n) operation

        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            
            if x == y:
                continue
            else:
                heapq.heappush(stones, (y-x))
        
        return -stones[0] if stones else 0
