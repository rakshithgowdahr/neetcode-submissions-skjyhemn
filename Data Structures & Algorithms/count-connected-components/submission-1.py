class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        components = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        for ver in range(n):
            if ver not in visited:
                dfs(ver)
                components += 1
        return components