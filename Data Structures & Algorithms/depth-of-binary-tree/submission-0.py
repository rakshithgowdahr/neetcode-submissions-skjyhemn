# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current_node = root
        stack = []
        if current_node:
            stack.append([current_node, 1])
        height = 0
        while len(stack):
            node, h = stack.pop()
            height = max(height, h)
            if node.left:
                stack.append([node.left, h+1])
            if node.right:
                stack.append([node.right, h+1])
        return height