class Trie:
    def __init__(self):
        self.children = {}
        self.word = ""
class Solution:
    def __init__(self):
        self.trie = Trie()
    def insert(self, word):
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        n = len(board)
        m = len(board[0])
        def dfs(i, j, trie_node, output):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            ch = board[i][j]
            if ch not in trie_node.children:
                return
            trie_node = trie_node.children[ch]
            if trie_node.word != "":
                output.append(trie_node.word)
                trie_node.word = ""
            board[i][j] = "#"
            dfs(i+1, j, trie_node, output)
            dfs(i-1, j, trie_node, output)
            dfs(i, j+1, trie_node, output)
            dfs(i, j-1, trie_node, output)
            board[i][j] = ch
            return
        res = []
        for i in range(n):
            for j in range(m):
                output = []
                dfs(i, j, self.trie, output)
                res = res + output
        return res



