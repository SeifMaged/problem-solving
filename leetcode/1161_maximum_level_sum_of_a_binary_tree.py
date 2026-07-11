# O(n) time, each node is processes once
# O(n) space, in case of a full BST, the final level has n/2 nodes to be stored in the queue

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = deque()
        if root:
            level.append(root)
        
        max_level = float('-inf')
        max_level_index = -1

        index = 0
        while level:
            current_level = 0
    
            for i in range(len(level)):
                node = level.popleft()
                current_level += node.val

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if current_level > max_level:
                max_level_index = index+1
                max_level = current_level
            
            index += 1
        
        return max_level_index