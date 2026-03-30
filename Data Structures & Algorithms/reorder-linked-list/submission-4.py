# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half_ll = slow.next
        slow.next = None
        prev_node = None
        current_node = second_half_ll
        while current_node:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp
        second_half_ll = prev_node
        c1 = head
        c2 = second_half_ll
        main_ll = head
        while c1 and c2:
            temp1 = c1.next
            temp2 = c2.next
            main_ll.next = c2
            main_ll = main_ll.next
            c1 = temp1
            main_ll.next = c1
            main_ll = main_ll.next
            c2 = temp2