# Easy
# Binary Tree - Depth First Search
# O(n) Time, where n is the number of nodes in the binary tree
# O(h) Space, where h is the height of the binary tree

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []

        def helper(root):
            if root:
                helper(root.left)
                output.append(root.val)
                helper(root.right)
        
        helper(root)
            
        return output