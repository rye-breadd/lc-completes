"""
b is a dependency of a
[0, 1, 2, ..., n]

Khan's algorithm b/c of topological sorting + cycle detection

We need to detect a cycle in the courses & we need to start at the course that is not a dep for any other


0 -> 1 -> 2 -> 0

Input: numCourses = 3, prerequisites = [[0, 1], [1, 2], [2, 0]]
deg = [1, 1, 1]
adj = {0 : 1, 1 : 2, 2: 0}
visit = ()
q = []
course = 

0 -> 1
  -> 2

deg = [0, 0, 0]
adj = {0: [1, 2]}
visit = (0,1,2)
q = [2]
course = 0

"""
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees = [0] * numCourses
        adj = defaultdict(list)

        for curr, pre in prerequisites:
            adj[curr].append(pre)
            degrees[pre] += 1
        
        finish = 0
        q = deque()
        for i, amt in enumerate(degrees):
            if amt == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            finish += 1
        
            for c in adj[course]:
                
                degrees[c] -= 1
                if degrees[c] == 0:
                    q.append(c)
            
        return finish == numCourses
                    
        
                    
"""
Time Complexity: O(V + E) where V = verticies, E = edges
Space Complexity: O(V + E)

Solution: Khan's algorithm --> topological sort

How did you know?
Needed to start at course that no other courses needed as a dependency --> topological sorting

Finding a cycle --> only 0 degree is added to queue, cycles will always have a degree of 1, so never traveled to

"""
                    
                

        
            
            



        
        
        