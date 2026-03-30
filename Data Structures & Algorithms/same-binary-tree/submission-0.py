# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = []
        q_stack = []
        current_p = p
        current_q = q
        if current_p:
            p_stack.append(current_p)
        if current_q:
            q_stack.append(current_q)
        while len(p_stack) and len(q_stack):
            p_node, q_node = p_stack.pop(), q_stack.pop()
            if (p_node and not q_node) or (q_node and not p_node) or (p_node.val != q_node.val):
                return False
            if (p_node.left and not q_node.left) or (q_node.left and not p_node.left):
                return False
            if p_node.left:
                p_stack.append(p_node.left)
                q_stack.append(q_node.left)
            if (p_node.right and not q_node.right) or (q_node.right and not p_node.right):
                return False
            if p_node.right:
                p_stack.append(p_node.right)
                q_stack.append(q_node.right)
        return len(p_stack) == len(q_stack)