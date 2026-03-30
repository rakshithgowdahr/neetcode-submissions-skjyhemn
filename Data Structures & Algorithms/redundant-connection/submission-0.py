class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visited = set()
        cycle = set()
        cycleStart = None
        def dfs(curr, prev):
            nonlocal cycleStart
            if curr in visited:#cycle found
                cycleStart = curr
                return True
            visited.add(curr)
            for nei in adj[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr):
                    if cycleStart != None:
                        cycle.add(curr)
                    if curr == cycleStart:
                        cycleStart = None
                    return True
            return False
        dfs(1, None)
        for v1, v2 in edges[::-1]:
            if v1 in cycle and v2 in cycle:
                return [v1, v2]
