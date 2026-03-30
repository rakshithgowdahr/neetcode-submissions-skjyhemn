class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in range(numCourses):
            adj[i] = []
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
        visited = set()
        def dfs(c):
            if len(adj[c]) == 0:
                return True
            if c in visited:
                return False
            visited.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            adj[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        