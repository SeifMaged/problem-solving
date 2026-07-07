# leetcode 15. 3Sum
# https://leetcode.com/problems/3sum/
# Medium
# O(n^2) time, O(1) space

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if i > 0 and num1 == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums)-1
            
            while left < right:
                threeSum = num1 + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num1, nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            
        return result