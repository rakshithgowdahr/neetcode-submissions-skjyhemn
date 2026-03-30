# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_node = root
        stack = []
        if current_node:
            stack.append(current_node)
        while len(stack):
            node = stack.pop()
            copy_right = None
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                copy_right = node.right
            node.right = node.left
            node.left = copy_right
        return root