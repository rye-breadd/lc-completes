# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            nonlocal res
            
            if not node:
                return
        
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
    
        dfs(root)
        return res[k - 1]
            
"""
res = [2, 3, 4, 5]
dfs(4)
dfs(3) =
dfs(2) 
dfs(None) = none
"""


        
        