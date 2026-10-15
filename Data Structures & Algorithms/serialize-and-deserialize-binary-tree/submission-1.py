# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
center, left, right

12nonenone


"""

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        print(",".join(res))
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        s = data.split(',')
        i = 0


        def dfs():
            nonlocal i
            if s[i] == "N":
                i += 1
                return
            
            node = TreeNode(int(s[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
            

            
        
        
