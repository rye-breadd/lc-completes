# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

p and q > curr = go right
p and q < cuur = go left
else:
    = p or q:
        check left and right to see 
    
    we at the end
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if (p.val < q.val < root.val) or (q.val < p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (root.val < p.val < q.val) or (root.val < q.val < p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
                
                


        


        