# Divide and Conquer
# Recursion
# O(log n) Time complexity
# O(log n) Space complexity due to recursion stack
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        if n % 2 == 0:
            temp = self.myPow(x, n//2)
            return temp * temp
        else:
            temp = self.myPow(x, n//2)
            return x * temp * temp        