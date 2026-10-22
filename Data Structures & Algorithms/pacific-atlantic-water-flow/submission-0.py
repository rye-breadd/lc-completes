class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        
        def dfs(r, c, ocean, prev_val):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean:
                return

            if heights[r][c] < prev_val:
                return
            
            ocean.add((r, c))
            adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for ar, ac in adj:
                dfs(ar, ac, ocean, heights[r][c])

        # pacific 
        p = set()
        for c in range(COLS):
            dfs(0, c, p, -1)
        for r in range(ROWS):
            dfs(r, 0, p, -1)

        a = set()
        for c in range(COLS):
            dfs(ROWS - 1, c, a, -1)
        for r in range(ROWS):
            dfs(r, COLS - 1, a, -1)

        res = []
        for i in p:
            if i in a:
                res.append(i)
        
        return res
        
        

        
        