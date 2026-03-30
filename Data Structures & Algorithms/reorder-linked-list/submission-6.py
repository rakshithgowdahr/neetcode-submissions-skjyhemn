# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #calculate length
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next
        #break the list
        count = 0
        node = head
        list2 = None
        while node:
            count += 1
            if count > (list_len//2):
                list2 = node.next
                node.next = None
            node = node.next
        #reverse the list2
        curr_node = list2
        prev = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        #merge the list
        c1, c2 = head, prev
        while c1 and c2:
            c1_next = c1.next
            c2_next = c2.next
            c1.next = c2
            c2.next = c1_next
            c1 = c1_next
            c2 = c2_next