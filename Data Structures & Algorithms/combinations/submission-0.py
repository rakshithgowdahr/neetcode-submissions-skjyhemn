class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, hash_set):
            if len(subset) == k:
                res.append(subset.copy())
                return
            for j in range(i, n+1):
                if j not in hash_set:
                    subset.append(j)
                    hash_set.add(j)
                    backtrack(j+1, subset, hash_set)
                    hash_set.remove(j)
                    subset.pop()
        backtrack(1, [], set())
        return res