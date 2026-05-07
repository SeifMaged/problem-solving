# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Medium
# O(n) time, O(1) space
# Sliding Window

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        running_sum = 0
        left = 0
        sol = 0
        
        for i in range(k-1):
            running_sum += arr[i]
        
        for right in range(k-1, len(arr)):
            running_sum += arr[right]
            
            if right - left + 1 > k:
                running_sum -= arr[left]
                left += 1
            
            if (running_sum / k) >= threshold:
                sol += 1
            
        return sol