"""

d o g
  i f f


"""


class Node:
    def __init__(self, end=False):
        self.end = end
        self.desc = [None] * 26

class PrefixTree:

    def __init__(self):
        self.nodes = Node()

    def insert(self, word: str) -> None:
        curr = self.nodes
        for i in range(len(word)):
            letter_idx = ord(word[i]) - ord('a')

            if curr.desc[letter_idx] == None:
                curr.desc[letter_idx] = Node()

            curr = curr.desc[letter_idx]
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.nodes
        for i in range(len(word)):
            letter_idx = ord(word[i]) - ord('a')

            if curr.desc[letter_idx] == None:
                return False

            curr = curr.desc[letter_idx]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.nodes
        for i in range(len(prefix)):
            letter_idx = ord(prefix[i]) - ord('a')

            if curr.desc[letter_idx] == None:
                return False

            curr = curr.desc[letter_idx]

        return True