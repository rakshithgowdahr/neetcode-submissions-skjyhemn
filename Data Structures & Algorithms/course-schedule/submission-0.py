class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i:[] for i in range(numCourses)}
        for s, d in prerequisites:
            adj[s].append(d)
        visited = set()
        def DFS(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            visited.add(course)
            for crs in adj[course]:
                if not DFS(crs):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        for i in range(numCourses):
            if not DFS(i):
                return False
        return True