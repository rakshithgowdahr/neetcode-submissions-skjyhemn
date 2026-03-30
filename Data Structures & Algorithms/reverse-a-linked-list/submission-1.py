# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        # 0 <- 1  2 -> 3
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next #1
            current_node.next = prev_node # 0 -> None
            prev_node = current_node # 0
            current_node = next_node
        return prev_node
