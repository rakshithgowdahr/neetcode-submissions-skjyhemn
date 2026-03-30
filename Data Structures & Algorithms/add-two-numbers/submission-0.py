# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1_node = l1
        c2_node = l2
        s1, s2 = [], []
        while c1_node or c2_node:
            if c1_node:
                s1.append(c1_node.val)
                c1_node = c1_node.next
            if c2_node:
                s2.append(c2_node.val)
                c2_node = c2_node.next
        i, j = 0, 0
        final_sum = []
        carry = 0
        while i < len(s1) or j < len(s2):
            num1 = num2 = 0
            if i < len(s1):
                num1 = s1[i]
                i += 1
            if j < len(s2):
                num2 = s2[j]
                j += 1
            if num1+num2+carry < 10:
                final_sum.append(num1+num2+carry)
                carry = 0
            else:
                carry = (num1+num2+carry) - 10
                final_sum.append(carry)
                carry = 1
        if carry:
            final_sum.append(carry)
        new_ll = ListNode(0)
        prev_node = new_ll
        for num in final_sum:
            new_node = ListNode(num)
            prev_node.next = new_node
            prev_node = new_node
        return new_ll.next