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

from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = []
        output = []

        if root:
            level.append(root)

        
        while level:
            next_level = []
            current_values = []

            for node in level:
                current_values.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
            output.append(current_values)
            level = next_level
        
        return output