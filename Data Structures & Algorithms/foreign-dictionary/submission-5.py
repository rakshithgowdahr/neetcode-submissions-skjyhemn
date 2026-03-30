class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minL = min(len(word1), len(word2))
            if word1[:minL] == word2[:minL] and len(word1) > len(word2):
                return ""
            for j in range(minL):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        print(adj)
        visited = dict()
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])