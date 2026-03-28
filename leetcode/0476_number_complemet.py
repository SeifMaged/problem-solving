#O(1) Time
#O(1) Space
class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1 
        
        return num ^ mask # xor number with 1s to get complement
