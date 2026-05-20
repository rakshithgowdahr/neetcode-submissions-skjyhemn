# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, node, output):
        if not node:
            return output
        self.postorder(node.left, output)
        self.postorder(node.right, output)
        output.append(node.val)
        return output
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorder(root, [])