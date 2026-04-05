# Counting
# O(N) Time
# O(1) Space
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count = 0
        right_count = 0
        wildcard_count = 0

        for move in moves:
            if move == 'L':
                left_count += 1
            elif move == 'R':
                right_count += 1
            else:
                wildcard_count += 1
        
        return abs(left_count - right_count) + wildcard_count