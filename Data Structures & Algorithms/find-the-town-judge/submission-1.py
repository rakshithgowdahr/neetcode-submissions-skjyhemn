class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        people_set = set()
        for t in trust:
            people_set.add(t[0])
            adj_list[t[0]].append(t[1])
            adj_list[t[1]].append(t[0])
        for i in range(1, n+1):
            if i not in people_set and len(adj_list[i]) == n-1:
                return i
        return -1
        