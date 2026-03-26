# Leetcode 2169 - Count Operations to Obtain Zero
# Solved Using Euclidean algorithm
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while num1 and num2:
            # Doesn't matter which number is actually bigger, after 1 iteration will swap in case num2 is bigger
            count += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1

        return count
