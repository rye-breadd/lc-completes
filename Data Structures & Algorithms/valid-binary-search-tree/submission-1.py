# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
perform a dfs


           3
      2            7
    1   10     5       8
             4   6

6: (3, inf)
5: (3, 7)
4: (3, 5)

we need to update regardless of max or min

left < node < right

"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
    
        def dfs(node, left, right):
            nonlocal is_valid
            if not node:
                return

            
            if node.left and (left >= node.left.val or node.left.val >= node.val):
                is_valid = False
                return
            
            if node.right and (right <= node.right.val or node.right.val <= node.val):
                is_valid = False
                return
                
            dfs(node.left, left, node.val)
            dfs(node.right, node.val, right)
            
        dfs(root, float("-inf"), float("inf"))
        return is_valid 
                
"""


           3
      2            7
    1   10     5       8


dfs(7, 3, inf)

"""