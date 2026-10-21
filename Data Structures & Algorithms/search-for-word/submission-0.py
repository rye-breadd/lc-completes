class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        has_word = False
        visited = set()
        def backtrack(r, c, idx):
            nonlocal has_word
            if idx >= len(word) - 1:
                has_word = True
                return
            
            directions = [(r + 1,c), (r - 1,c), (r,c + 1), (r,c - 1)]
            for ar, ac in directions:
                if ar >= 0 and ar < ROWS and ac >= 0 and ac < COLS and (ar, ac) not in visited:
                    if board[ar][ac] == word[idx + 1]:
                        visited.add((ar,ac))
                        print(board[ar][ac])
                        backtrack(ar, ac, idx + 1)
                        visited.remove((ar, ac))
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    print('board start', word[0])
                    visited.add((r,c))
                    backtrack(r, c, 0)
                    visited.remove((r,c))
        
        return has_word
