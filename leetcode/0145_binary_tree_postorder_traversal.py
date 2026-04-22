# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Easy
# O(n) Time, where n is the number of nodes in the binary tree
# O(h) Space, where h is the height of the binary tree
# Binary Tree - Depth First Search

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                output.append(root.val)
        
        postorder(root)
        return output