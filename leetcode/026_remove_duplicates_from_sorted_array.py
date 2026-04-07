# Easy
# Array/List
# O(n) Time, where n is the length of nums
# O(1) Space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        prev = None

        for num in nums:
            if num != prev:
                nums[left] = num
                left += 1
                prev = num
        
        return left