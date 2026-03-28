# Hashmap
# O(n) time
# O(1) space
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        freq = {}

        for char in s:
            prevFreq = freq.get(char, 0)
            if prevFreq == 1:
                return char
            freq[char] = 1 + prevFreq
        
        return -1
