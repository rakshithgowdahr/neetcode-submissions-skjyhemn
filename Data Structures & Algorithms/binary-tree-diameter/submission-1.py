# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = 0
    def DFS(self, node):
        if not node:
            return 0
        left = self.DFS(node.left)
        right = self.DFS(node.right)
        self.result = max(self.result, left+right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.result