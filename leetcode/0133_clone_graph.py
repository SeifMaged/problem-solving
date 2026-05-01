# 133. Clone Graph
# leetcode.com/problems/clone-graph/
# Medium
# O(V + E) time, O(V) space, where V is the number of nodes in the graph and E is the number of edges
# Breadth First Search
# We can use breadth first search (BFS) to traverse the graph and create a copy of it.
# We will maintain a mapping from the original nodes to the new nodes that we create.
# We will start from the given node and explore its neighbors. For each neighbor, if
# it has not been visited before, we will create a new node for it and add it to the
# queue for BFS. We will also add the new node to the neighbors of the current node in
# the new graph. Finally, we will return the new node corresponding to the given node.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[current].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]