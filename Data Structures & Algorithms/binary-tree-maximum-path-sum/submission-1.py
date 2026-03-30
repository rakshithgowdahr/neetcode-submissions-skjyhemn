# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_sum = -float("inf")
    def postorder(self, node):
        if not node:
            return 0
        # print('val', node.val)
        left_sum = self.postorder(node.left)
        # print('left_sum', left_sum)
        right_sum = self.postorder(node.right)
        # print('right_sum', right_sum)
        self.max_sum = max(self.max_sum, node.val, node.val+left_sum+right_sum, node.val+left_sum, node.val+right_sum)
        # print('max_sum', self.max_sum)
        return max(node.val, node.val+left_sum, node.val+right_sum)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.max_sum