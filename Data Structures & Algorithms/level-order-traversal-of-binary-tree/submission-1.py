# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def BFS(self, node, output, h):
        if not node:
            return output
        if len(output) < h:
            output.append([])
        output[h-1].append(node.val)
        self.BFS(node.left, output, h+1)
        self.BFS(node.right, output, h+1)
        return output
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.BFS(root, [], 1)