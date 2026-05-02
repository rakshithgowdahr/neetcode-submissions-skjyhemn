# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left-1):
            pre = pre.next
        cur = pre.next
        for _ in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy_node.next