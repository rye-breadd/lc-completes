class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0  or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            res = 1
            grid[r][c] = 0
            
            adj = [(r + 1,c),(r - 1,c),(r,c + 1),(r,c - 1)]
            for ar, ac in adj:
                res += dfs(ar, ac)

            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
            

        