# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareTree(m_node, s_node) -> bool:
            if m_node == s_node:
                return True
            if (m_node and not s_node) or (s_node and not m_node) or (m_node and s_node and m_node.val != s_node.val):
                return False
            return compareTree(m_node.left, s_node.left) and compareTree(m_node.right, s_node.right)
        isSubTree = False
        stack = [root]
        while len(stack):
            node = stack.pop()
            if compareTree(node, subRoot):
                isSubTree = True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return isSubTree