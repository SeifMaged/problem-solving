# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_index = 0

        def dfs(low, high):
            if low > high:
                return None
            
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(low, mid-1)
            root.right = dfs(mid + 1, high)

            return root
        
        return dfs(0, len(inorder)-1)