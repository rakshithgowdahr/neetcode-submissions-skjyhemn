class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for frm, to in tickets:
            adj[frm].append(to)
        for key in adj:
            adj[key].sort()
        res = ["JFK"]
        def dfs(airport):
            if len(res) == len(tickets)+1:
                return True
            for index, dest in enumerate(adj[airport]):
                if dest == None:
                    continue
                res.append(dest)
                adj[airport][index] = None
                if dfs(dest):
                    return True
                res.pop()
                adj[airport][index] = dest
        dfs("JFK")
        return res