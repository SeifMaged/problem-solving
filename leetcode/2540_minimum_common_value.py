# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/
# O(n + m) time, O(1) space
# Topics: Array, Two Pointers

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n = len(nums1)
        m = len(nums2)
        smallest_common = float('inf')

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                smallest_common = min(smallest_common, nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return -1 if smallest_common == float('inf') else smallest_common
