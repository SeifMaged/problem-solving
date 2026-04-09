# Easy
# Dynamic Programming OR Recursion
# O(1) Space

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a = 1 # representing F(n-1)
        b = 0 # representing F(n-2)

        for i in range(2, n):
            a, b = a + b, a
        
        return a + b # Return F(n-1) + F(n-2)

    def fib_2(self, n: int) -> int: # O(2^n) Time, O(n) Space
        if n == 0 or n == 1:
            return n

        return self.fib_2(n-1) + self.fib_2(n-2)
        