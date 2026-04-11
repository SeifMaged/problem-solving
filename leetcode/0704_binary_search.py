# Easy
# Binary Search
# O(log n) Time, where n is the length of nums
# O(1) Space

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1