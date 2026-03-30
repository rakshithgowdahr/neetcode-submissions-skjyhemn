# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS(self, node, output):
        if not node:
            return output
        self.DFS(node.left, output)
        output.append(node.val)
        self.DFS(node.right, output)
        return output
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sorted_list = self.DFS(root, [])
        for i in range(1, len(sorted_list)):
            if sorted_list[i-1] >= sorted_list[i]:
                return False
        return True