# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []
        def DFS(node):
            nonlocal sorted_array
            if not node:
                return
            if node.left:
                DFS(node.left)
            sorted_array.append(node.val)
            if node.right:
                DFS(node.right)
        DFS(root)
        return sorted_array[k-1]