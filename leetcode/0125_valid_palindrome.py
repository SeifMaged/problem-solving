# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Easy
# O(n) time, O(1) space, where n is the length of the string and the space is O(1) because we are only using a few pointers and variables
# Two Pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNum(char):
            if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')) or (ord('0') <= ord(char) <= ord('9')):
                return True
            return False

        left, right = 0, len(s)-1
        while left < right:
            while left < right and not isAlphaNum(s[left]):
                left += 1
            while left < right and not isAlphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -=1

        return True