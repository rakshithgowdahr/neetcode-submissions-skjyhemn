# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        que = deque()
        if p and q:
            que.append((p, q))
        while que:
            l, r = que.popleft()
            if l.val != r.val:
                return False
            if l.left or r.left:
                if (l.left and not r.left) or (r.left and not l.left):
                    return False
                que.append((l.left, r.left))
            if l.right or r.right:
                if (l.right and not r.right) or (r.right and not l.right):
                    return False
                que.append((l.right, r.right))
        return True