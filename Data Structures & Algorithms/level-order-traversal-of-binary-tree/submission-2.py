# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = None
        if(root):
            queue = [(root, 0)]
        while queue:
            node, h = queue.pop(0)
            if len(output) <= h:
                output.append([])
            output[h].append(node.val)
            if node.left:
                queue.append((node.left, h+1))
            if node.right:
                queue.append((node.right, h+1))
        return output