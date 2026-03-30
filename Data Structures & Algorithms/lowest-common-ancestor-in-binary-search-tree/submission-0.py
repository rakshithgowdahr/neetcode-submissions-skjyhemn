# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, p, q):
        if node and (node.val == p.val or node.val == q.val):
            return node
        if node and node.val > p.val and node.val < q.val:
            return node
        if node and node.val < p.val and node.val > q.val:
            return node
        if node and p.val < node.val and q.val < node.val:
            return self.traverse(node.left, p, q)
        else:
            return self.traverse(node.right, p, q)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse(root, p, q)