# O(N^2) Time
# O(N) Space
# Interview Microsoft Question 2
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s 