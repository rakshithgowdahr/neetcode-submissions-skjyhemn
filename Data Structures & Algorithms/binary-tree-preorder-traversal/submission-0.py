# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, output):
        if not node:
            return output
        output.append(node.val)
        self.preorder(node.left, output)
        self.preorder(node.right, output)
        return output
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorder(root, [])