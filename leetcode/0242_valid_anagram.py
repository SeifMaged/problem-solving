# Hashmap
# Easy
# O(n) Time
# O(n) Space

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char,0)
        
        for char in t:
            char_count = freq.get(char, 0) 
            if char_count == 0:
                return False
            else:
                freq[char] = char_count - 1
        
        return True
