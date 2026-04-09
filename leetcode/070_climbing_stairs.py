# Easy
# Dynamic Programming / Recursion
# Similar to Fibonacci Number
# O(1) Space

class Solution: 
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev = 2
        prev2 = 1

        for i in range(2, n):
            prev, prev2 = prev + prev2, prev
        
        return prev

    memo = {}
    def climbStairs_2(self, n: int) -> int:
        global memo
        if n == 1 or n == 2:
            return n
        if n not in self.memo:
            self.memo[n] = self.climbStairs_2(n-1) + self.climbStairs_2(n-2)
        return self.memo[n]

