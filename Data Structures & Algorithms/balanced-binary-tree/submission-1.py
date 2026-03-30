# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = True
    def DFS(self, node):
        if not node or self.result == False:
            return 0
        left = self.DFS(node.left)
        right = self.DFS(node.right)
        if abs(left-right) > 1:
            self.result = False
        return 1 + max(left, right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.DFS(root)
        return self.result