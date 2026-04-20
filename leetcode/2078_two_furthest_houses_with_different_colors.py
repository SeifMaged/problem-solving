# 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# Easy
# O(n^2) time, O(1) space
# Greedy
# Daily Problem 20/04/2026

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0

        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    max_dist = max(max_dist, j-i)
        
        return max_dist