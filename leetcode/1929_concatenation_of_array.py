# Easy
# Array/List - Dynamic Lists
# O(n) Time, where n is the length of nums
# O(n) Space, where n is the length of nums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
        # for i in range(len(nums)):
        #     nums.append(nums[i])
        
        # return nums