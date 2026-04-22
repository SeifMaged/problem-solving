# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/
# Medium
# O(h) time, O(h) space, where h is the height of the tree
# Binary Search Tree, Recursion

from typing import Optional
# Definition for a binary tree node.

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.get_min_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root

        
    def get_min_node(self, root):

        trav = root
        while trav and trav.left:
            trav = trav.left
        
        return trav