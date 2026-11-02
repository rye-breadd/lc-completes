class TrieNode:
    def __init__(self):
        self.end = False
        self.word = None
        self.childs = {}

class Trie:
    def __init__(self):
        self.nodes = TrieNode()
    
    def add(self, word):
        curr = self.nodes
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = TrieNode()
            curr = curr.childs[c]
        curr.end = True
        curr.word = word

    def search(self, word):
        curr = self.nodes
        for c in word:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return curr.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = Trie()
        for w in words:
            d.add(w)
        
        visit = set()
        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit 
                or board[r][c] not in node.childs):
                return False

            visit.add((r,c))
            curr = board[r][c]
            curr_node = node.childs[curr]
            if curr_node.end:
                res.add(curr_node.word)
                curr_node.end = False

            adj = [(r + 1,c),(r - 1,c),(r,c + 1),(r,c - 1)]
            for ar, ac in adj:
                dfs(ar, ac, curr_node)

            visit.remove((r,c))


        res = set()
        ROWS = len(board)
        COLS = len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, d.nodes)
        return list(res)
        