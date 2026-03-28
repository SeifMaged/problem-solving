# Bit manipulation
# O(1) time
# O(1) space
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal # xor start with goal
        return xor.bit_count() # built in method in python to count the bits that are still set to 1 after the result, since this is the result of the xor, it will show the different bits

