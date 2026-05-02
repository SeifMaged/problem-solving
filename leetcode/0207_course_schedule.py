# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Medium
# O(V + E) time, O(V) space, where V is the number of
# courses and E is the number of prerequisites
# Depth First Search
# Cycles in a directed graph can be detected using depth first search (DFS). 
# We will maintain a set of courses that are currently being visited in the DFS. 
# If we encounter a course that is already being visited, it means there is a cycle 
# in the graph and we cannot finish all courses. If we successfully visit all courses 
# without encountering a cycle, it means we can finish all courses.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            
            adjList[course].append(prerequisite)
        
        visiting = set()

        def dfs(course):
            if course in visiting: # Cycle
                return False
            if adjList[course] == []:
                return True

            visiting.add(course)
            for prerequisite in adjList[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            adjList[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        