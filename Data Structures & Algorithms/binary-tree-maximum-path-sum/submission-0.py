# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = -1001
    def DFS(self, node, max_sum,):
        if not node:
            return [max_sum]
        left = self.DFS(node.left, max_sum)
        right = self.DFS(node.right, max_sum)
        curr_max = max(node.val, node.val+left[0], node.val+right[0])
        self.max = max(self.max, node.val, node.val+left[0], node.val+right[0], node.val+left[0]+right[0])
        return [curr_max]
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = self.DFS(root, -1001)
        return self.max