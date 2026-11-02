"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


        clone = {
            1 : node(1,[node(2)])
            2 : node(2,[node(1), node(3)])
            3 : node(3, [node(2)])
        }
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            
            clone[node] = Node(val=node.val,neighbors=[])
            for nei in node.neighbors:
                clone[node].neighbors.append(dfs(nei))

            return clone[node]

        return dfs(node) if node else None

            
            
        


                