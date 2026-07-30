class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        visited = [False] * n
        def DFS(i):
            visited[i] = True
            for nei in range(n):
                if isConnected[i][nei] and visited[nei] == False:
                    DFS(nei)
        for i in range(n):
            if not visited[i]:
                DFS(i)
                res += 1
        return res