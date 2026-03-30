# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        stack = [(root, root.val)]
        while len(stack):
            node, curr_max = stack.pop()
            if node.val >= curr_max:
                output += 1
                curr_max = node.val
            if node.left:
                stack.append((node.left, curr_max))
            if node.right:
                stack.append((node.right, curr_max))
        return output