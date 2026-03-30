# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = 0
    def traverse(self, node, prev_max):
        if not node:
            return
        if node.val >= prev_max:
            self.result += 1
            prev_max = node.val
        self.traverse(node.left, prev_max)
        self.traverse(node.right, prev_max)
    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, -float("inf"))
        return self.result