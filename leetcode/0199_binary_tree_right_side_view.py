# Medium
# Binary Tree - Breadth First Search
# O(n) Time, where n is the number of nodes in the binary tree
# O(n) Space, where n is the number of nodes in the binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        level = deque()
        output = []
        if root:
            level.append(root)

        while level:
            
            output.append(level[-1].val)

            for i in range(len(level)):
                if level[0].left:
                    level.append(level[0].left)
                if level[0].right:
                    level.append(level[0].right)
                level.popleft()
            

        return output