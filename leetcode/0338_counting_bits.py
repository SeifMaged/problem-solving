# Easy
# Bit Manipulation
# O(n) Time
# O(n) Space
# Using the bit_count() method to count the number of 1s in the binary representation of each number from 0 to n, we can efficiently populate the output list with the required counts.

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n+1):
            output[i] = i.bit_count()
        
        return output