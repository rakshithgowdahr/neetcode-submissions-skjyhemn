# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        if not head:
            return head
        next_node = None
        while current_node.next: #2 and 2 -> 3 is true
            next_node = current_node.next #3
            current_node.next = prev_node #2 -> 3 will be 3 -> 2
            prev_node = current_node # prev = 2
            current_node = next_node # curr = 3
            next_node = next_node.next
        current_node.next = prev_node
        return current_node