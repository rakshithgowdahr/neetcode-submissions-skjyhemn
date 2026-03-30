# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l_len = 0
        current_node = head
        while current_node:
            l_len += 1
            current_node = current_node.next
        to_be_removed = l_len - n
        counter = 0
        current_node = head
        prev_node = None
        while counter <= to_be_removed:
            if counter == to_be_removed:
                if counter != 0:
                    prev_node.next = current_node.next if current_node.next else None
                if counter == 0:
                    head = current_node.next
            prev_node = current_node
            current_node = current_node.next
            counter += 1
        return head

