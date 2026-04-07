# Easy
# Array/List
# O(n) Time, where n is the length of nums
# O(1) Space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0

        for num in nums:
            if num != val:
                nums[left] = num
                left += 1
        
        return left