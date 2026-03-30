# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def BFS(self, node, output, h):
        if not node:
            return node
        if h > len(output):
            output.append([])
        output[h-1].append(node.val)
        self.BFS(node.left, output, h+1)
        self.BFS(node.right, output, h+1)
        return output
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = self.BFS(root, [], 1)
        return [arr[-1] for arr in level]