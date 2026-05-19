# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# O(log n) time, O(n) space

import heapq

class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller, -1 * num)

        if self.larger and (-1 * self.smaller[0] > self.larger[0]):
            heapq.heappush(self.larger, -1 * heapq.heappop(self.smaller))
        
        if len(self.smaller) > len(self.larger) + 1:
            heapq.heappush(self.larger, -1 * heapq.heappop(self.smaller))
        
        if len(self.larger) > len(self.smaller) + 1:
            heapq.heappush(self.smaller, -1 * heapq.heappop(self.larger))


    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -1 * self.smaller[0]
        elif len(self.larger) > len(self.smaller):
            return self.larger[0]

        return (self.larger[0] + (-1 * self.smaller[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()