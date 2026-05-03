# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0] #[withRoot, withoutRoot]
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            rob = node.val + left_pair[1]+right_pair[1]
            skip = max(left_pair)+max(right_pair)
            return [rob, skip]
        return max(dfs(root))