class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie.children:
                trie.children[c] = Trie()
            trie = trie.children[c]
        trie.endOfWord = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return trie.endOfWord

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if c not in trie.children:
                return False
            trie = trie.children[c]
        return True
        