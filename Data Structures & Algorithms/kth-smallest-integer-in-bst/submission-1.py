# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, output):
        if not node:
            return
        self.traverse(node.left, output)
        output.append(node.val)
        self.traverse(node.right, output)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []
        self.traverse(root, sorted_list)
        return sorted_list[k-1]
