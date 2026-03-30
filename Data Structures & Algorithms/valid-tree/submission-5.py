class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, None):
            return False
        return len(visited) == n