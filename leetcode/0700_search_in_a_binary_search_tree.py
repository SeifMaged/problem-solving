# Easy
# Binary Search Tree
# O(h) Time, where h is the height of the binary search tree
# O(h) Space, where h is the height of the binary search tree
# Assuming the height of the binary search tree is h, the time complexity is O(h) because in the worst case, we may have to traverse from the root to a leaf node. The space complexity is also O(h) due to the recursive call stack in the worst case when the tree is skewed. In a balanced binary search tree, the height h would be log(n), where n is the number of nodes in the tree, leading to O(log n) time and space complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)