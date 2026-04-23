# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Easy
# O(n) time, O(h) space, where n is the number of nodes in the tree and h is the height of the tree
# Backtracking, Binary Tree, Depth First Search, Recursion
# If tree is balanced O(log n) space, if tree is skewed O(n) space
# O(n) time because we visit each node once, O(h) space because of the recursion stack


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def leaf_path(root, path):
            if not root:
                return False

            path += root.val

            if not root.left and not root.right and path == targetSum:
                return True
            return leaf_path(root.left, path) or leaf_path(root.right, path)
        
        return leaf_path(root, 0)