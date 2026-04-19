# Easy
# Hash Table, Queue
# O(n) Time, where n is the number of sandwiches. We iterate through the sandwiches and check if there are students who prefer that type of sandwich.
# O(1) Space. We use a Counter to store the frequency of students' preferences, which takes constant space since there are only two types of sandwiches (0 and 1).

from typing import Counter, List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        output = len(students)
        freq = Counter(students)

        for sandwich in sandwiches:
            if freq[sandwich] > 0:
                output -= 1
                freq[sandwich] -= 1
            else:
                break
        
        return output