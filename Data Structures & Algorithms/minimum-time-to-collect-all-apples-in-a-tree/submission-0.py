class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for e, v in edges:
            adj[e].append(v)
            adj[v].append(e)
        visited = set()
        def dfs(node):
            time = 0
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    subtree_time = dfs(nei)
                    if subtree_time or hasApple[nei]:
                        time += 2 + subtree_time
            return time
        return dfs(0)