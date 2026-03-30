# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, output, h):
        if not node:
            return output
        if h >= len(output):
            output.append([])
        output[h].append(node.val)
        if node.left:
            self.traverse(node.left, output, h+1)
        if node.right:
            self.traverse(node.right, output, h+1)
        return output
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        return self.traverse(root, [[]], 0)