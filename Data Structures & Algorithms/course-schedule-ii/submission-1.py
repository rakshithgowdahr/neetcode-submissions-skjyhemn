class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {course:[] for course in range(numCourses)}
        for course, pre in prerequisites:
            preReq[course].append(pre)
        output = []
        cycle = set()
        completed = set()
        def dfs(c) -> bool:
            if c in cycle:
                return False
            if c in completed:
                return True
            cycle.add(c)
            for pre in preReq[c]:
                if not dfs(pre):
                    return False
            output.append(c)
            cycle.remove(c)
            completed.add(c)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output