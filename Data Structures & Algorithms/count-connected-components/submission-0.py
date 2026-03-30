class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s,c in edges:
            adj[s].append(c)
            adj[c].append(s)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
        output = 0
        for i in range(0, n):
            if i not in visited:
                dfs(i)
                output += 1
        return output