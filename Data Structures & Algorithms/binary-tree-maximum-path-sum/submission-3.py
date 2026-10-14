# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
each node from the root, we want to take the max of it



"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        
        def dfs(node):
            nonlocal max_val
            if not node:
                return 0
            
            left_total = dfs(node.left)
            right_total = dfs(node.right)
            sub_total = node.val + left_total + right_total

            sub_right = right_total + node.val
            sub_left = left_total + node.val

            sub_total = max(sub_total, sub_right, sub_left)
            max_val = max(sub_total, max_val)

            return max(0, sub_left, sub_right)

        dfs(root)
        return max_val

        