
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        only one root
        root can reach any nodes
        there is no cycle
        """

        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visit = set()
        cycle = False
        def dfs(node, parent):
            nonlocal cycle
            visit.add(node)

            for nei in adj[node]:
                if nei in visit:
                    if nei != parent:
                        cycle = True
                        return
                    continue
                else:
                    dfs(nei, node)         
        dfs(0, 0)
        if cycle or len(visit) != n:
            return False
        return True 
            
