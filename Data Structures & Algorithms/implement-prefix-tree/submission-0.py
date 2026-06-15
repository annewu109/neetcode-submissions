class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if currNode.children[pos] == None:
                currNode.children[pos] = TrieNode()
            currNode = currNode.children[pos]
        currNode.endOfWord = True


    def search(self, word: str) -> bool:
        currNode = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if currNode.children[pos] == None:
                return False
            currNode = currNode.children[pos]
        if currNode.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            pos = ord(c) - ord('a')
            if currNode.children[pos] == None:
                return False
            currNode = currNode.children[pos]
        return True
        
        