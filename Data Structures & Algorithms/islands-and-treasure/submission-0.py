from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            
            adj = [(r + 1,c),(r - 1,c),(r,c + 1),(r,c - 1)]
        
            for ar, ac in adj:
                if ar < 0 or ac < 0 or ar >= ROWS or ac >= COLS or grid[ar][ac] != 2147483647:
                    continue
                
                q.append((ar, ac))
                grid[ar][ac] = grid[r][c] + 1
            
            
        
        
        