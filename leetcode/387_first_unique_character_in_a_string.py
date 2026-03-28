# Hashmap
#O(1) Space Complexity - Since the freq hashmap will at most grow to have a key value pair for all of the possible 26 keys, which is a constant
#O(n) Time Complexity
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
