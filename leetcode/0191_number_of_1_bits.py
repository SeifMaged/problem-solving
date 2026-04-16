# Easy
# Bit Manipulation
# O(1) Time
# O(1) Space

# The bit_count() method counts the number of 1s in the binary representation of n, which is exactly what we need to determine the Hamming weight.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
    
    # Alternative approach using bit manipulation
    def hammingWeight_2(self, n: int) -> int:
        count = 0
        
        while n:
            count += n & 1 # Increment count if the least significant bit is 1
            n >>= 1 # Right shift n to check the next bit
        
        return count