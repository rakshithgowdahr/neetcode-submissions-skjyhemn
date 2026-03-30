class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited = set()
        def dfs(prev, node):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj_list[node]:
                if nei == prev:
                    continue
                if not dfs(node, nei):
                    return False
            return True
        res = dfs(None, 0)
        return res and len(visited) == n
