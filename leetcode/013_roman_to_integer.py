# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# O(n) time, O(1) space
# Topics: String, Hash Map

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {"I": 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        n = len(s)
        output = 0

        for i in range(n):
            if i < n-1 and romanToInt[s[i]] < romanToInt[s[i+1]]:
                output -= romanToInt[s[i]]
            else:
                output += romanToInt[s[i]] 
        
        return output