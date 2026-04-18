# Easy
# Math

class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        mirror = 0
        temp = n

        while temp:
            mirror *= 10
            mirror += temp % 10
            temp //= 10
        
        return abs(mirror-n)