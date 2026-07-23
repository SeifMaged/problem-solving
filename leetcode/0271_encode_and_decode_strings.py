#https://neetcode.io/problems/string-encode-and-decode/question
# Medium
# String

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(f'{len(string)}#{string}')
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        
        return result