# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, output):
        if not node:
            return output
        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)
        return output
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root, [])