class Node:
    def __init__(self):
        self.end = False
        self.nodes = [None] * 26

class WordDictionary:

    def __init__(self):
        self.desc = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.desc
        for c in word:
            letter_idx = ord(c) - ord('a')
            if not curr.nodes[letter_idx]:
                curr.nodes[letter_idx] = Node()
            
            curr = curr.nodes[letter_idx]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(curr, idx):
            if idx == len(word):
                return curr.end
            
            c = word[idx]

            if c == '.':
                for l in curr.nodes:
                    if l and dfs(l, idx + 1):
                        return True
                return False
            else:
                letter_idx = ord(c) - ord('a')
                if curr.nodes[letter_idx]:
                    if dfs(curr.nodes[letter_idx], idx + 1):
                        return True
                return False

        return dfs(self.desc, 0)
        
