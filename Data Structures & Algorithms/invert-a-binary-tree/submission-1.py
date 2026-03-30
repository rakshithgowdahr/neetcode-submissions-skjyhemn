# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_node = root
        q = deque()
        if curr_node:
            q.append(curr_node)
        while q:
            node = q.popleft()
            tmp = node.right
            node.right = node.left
            node.left = tmp
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root