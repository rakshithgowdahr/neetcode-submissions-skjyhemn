# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 0
        curr_node = head
        while curr_node:
            ll_len += 1
            curr_node = curr_node.next
        rm_index = ll_len - n
        if rm_index == 0:
            return head.next
        # print(rm_index)
        counter = 0
        curr_node = head
        while curr_node:
            counter += 1
            if counter == rm_index:
                # print(curr_node.val)
                # next_node = curr_node.next
                # next_node.next = None
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        return head