class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            
            adj = [(r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)]
            for ar, ac in adj:
                dfs(ar, ac)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
    
        return count
        
"""
time = (r * c) 
"""

            
        