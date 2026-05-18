class Solution:
    def simplifyPath(self, path: str) -> str:
        # .. -> pop
        # . -> ignore
        stack = []
        path_split = path.split("/")
        for p in path_split:
            if p == "":
                continue
            if p == ".":
                continue
            elif p == "..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/"+"/".join(stack)