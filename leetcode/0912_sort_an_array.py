# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Medium
# O(n log n) time, O(n) space
# Merge Sort

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums)-1)
        
    def merge_sort(self, arr, low, high):
        if high - low + 1 <= 1:
            return arr
        
        middle = (low + high)//2
        self.merge_sort(arr, low, middle)
        self.merge_sort(arr, middle+1, high)

        self.merge(arr, low, high)

        return arr
    
    def merge(self, arr, low, high):

        middle = (low + high)//2

        left = arr[low : middle+1]
        right = arr[middle+1 : high+1]
        i, j, k = 0, 0, low
        n, m = len(left), len(right)

        while i < n and j < m:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < n:
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < m:
            arr[k] = right[j]
            j +=1 
            k += 1


    # Alternative Sorting Algorithm: Insertion Sort
    # O(n^2) time, O(1) space
    # Won't be efficient for large arrays, but can be useful for small or nearly sorted arrays
    
    def insertion_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j-=1

        
        return nums