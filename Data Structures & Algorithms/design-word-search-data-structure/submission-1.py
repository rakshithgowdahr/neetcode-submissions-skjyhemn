class Trie:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def DFS(i, node):
            if i == len(word):
                return node.endOfWord
            ch = word[i]
            if ch == ".":
                for c in node.children.values():
                    if DFS(i+1, c):
                        return True
                return False
            if ch not in node.children:
                return False
            return DFS(i+1, node.children[ch])

        return DFS(0, self.trie)
