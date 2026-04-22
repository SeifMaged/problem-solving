# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []

        def preorder(root):
            if root:
                output.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)

        return output