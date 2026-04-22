# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Medium
# O(n) time, O(n) space, where n is the number of nodes in the binary tree
# Binary Tree, Depth First Search, Recursion
# If tree is balanced O(log n) space, if tree is skewed O(n) space
# O(n) time because we visit each node once, O(n) space because of the recursion stack and the hashmap

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.postorder_index = len(postorder)-1

        def dfs(low, high):
            if low > high:
                return None

            root_val = postorder[self.postorder_index]
            self.postorder_index -= 1
            mid = indices[root_val]

            root = TreeNode(root_val)

            root.right = dfs(mid+1, high)
            root.left = dfs(low, mid-1)
            
            return root
        
        return dfs(0, len(inorder)-1)