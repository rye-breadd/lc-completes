from collections import defaultdict
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # parents of themselves
        self.rank = [0] * n

    def find(self, i): # finding the parent node
        if self.parent[i] == i:
            return i 
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1
            return True
        return False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c = DSU(n)
        for e1, e2 in edges:
            c.union(e1, e2)
    

        res = set()
        for i in range(n):
            res.add(c.find(i))
        return len(res)
            


    
        
        
        
        