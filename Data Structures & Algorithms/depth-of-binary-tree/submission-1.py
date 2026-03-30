# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_h = 0
        q = deque()
        q.append((root, 1))
        while q:
            node, h = q.popleft()
            max_h = max(max_h, h)
            if node.left:
                q.append((node.left, h+1))
            if node.right:
                q.append((node.right, h+1))
        return max_h