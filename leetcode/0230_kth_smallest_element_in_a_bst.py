# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Medium
# O(n) time, O(n) space, where n is the number of nodes in the binary tree
# Binary Tree, Depth First Search, Recursion
# If tree is balanced O(log n) space, if tree is skewed O(n) space

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Iterative Inorder Traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
             
            curr = node.right
    
    # Recursive Inorder Traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        values = []

        def inorder(root):
            if root:
                inorder(root.left)
                values.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return values[k-1]