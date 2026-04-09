# Easy
# Dynamic Programming
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