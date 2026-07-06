# leetcode 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Medium
# O(n) time, O(h) space

from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, minimum, maximum):
            if root:
                if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val) or (root.val <= minimum) or (root.val >= maximum):
                    return False

                return helper(root.left, minimum, root.val) and helper(root.right, root.val, maximum)
            
            return True

        return helper(root, float("-inf"), float('inf'))