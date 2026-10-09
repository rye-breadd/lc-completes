# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        valid_level = 0
        res = []
        
        def dfs(node, level):
            nonlocal valid_level
            nonlocal res
            if not node:
                return

            if level >= valid_level:
                valid_level += 1
                res.append(node.val)
        
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return res
"""
valid_level = 3
res = [1, 3, 4, 5]

dfs:
(1,0)
(3,1)
(2,1)
(4,2)
(5,3)





"""
    
            
                      