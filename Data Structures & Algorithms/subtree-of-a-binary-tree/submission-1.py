# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, p, q):
        if (p and not q) or (q and not p):
            return False
        que = deque()
        if p and q:
            que.append((p, q))
        while que:
            p, q = que.popleft()
            if p.val != q.val:
                return False
            if p.left or q.left:
                if (p.left and not q.left) or (q.left and not p.left):
                    return False
                que.append((p.left, q.left))
            if p.right or q.right:
                if (p.right and not q.right) or (q.right and not p.right):
                    return False
                que.append((p.right, q.right))
        return len(que) == 0
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if self.isEqual(node, subRoot):
                return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right) 
        return False