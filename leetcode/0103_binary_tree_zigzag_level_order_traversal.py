# Medium
# Binary Tree - Breadth First Search
# O(n) Time, where n is the number of nodes in the binary tree
# O(n) Space, where n is the number of nodes in the binary tree

from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        reverse = False
        level = deque([root] if root else [])
        output = []
        
        while level:
            n = len(level)
            current_level = [0]*n

            for i in range(n):
                
                node = level.popleft()
            
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)  

                index = n - i - 1 if reverse else i
                current_level[index] = node.val
                
            reverse = not reverse
            output.append(current_level)
    
        return output
            

# Without Deque
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         reverse = False
#         level = []
#         output = []

#         if root:
#             level.append(root)
        

#         while level:

#             current_level = []
#             next_level = []

#             n = len(level)

#             for i in range(n):
                
#                 node = level[i]
            
#                 if node.left: next_level.append(node.left)
#                 if node.right: next_level.append(node.right)  
                
#                 if reverse:
#                     current_level.append(level[n-i-1].val)
#                 else:
#                     current_level.append(node.val)

                
                
#             reverse = not reverse
#             level = next_level
#             output.append(current_level)
    
#         return output
            