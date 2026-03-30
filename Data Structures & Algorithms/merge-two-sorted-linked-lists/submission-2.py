# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 or not list2:
            return list1 if list1 else list2
            
        curr_node1 = list1
        curr_node2 = list2
        
        while curr_node1 and curr_node2:
            next_node1 = curr_node1.next
            next_node2 = curr_node2.next
            
            if curr_node1.val <= curr_node2.val:
                # Check if curr_node2 fits between curr_node1 and next_node1
                if not next_node1 or curr_node2.val < next_node1.val:
                    curr_node1.next = curr_node2
                    # FIX: Swap the pointers effectively
                    curr_node1 = curr_node2  # Advance to the connected node
                    curr_node2 = next_node1  # The detached part becomes the other list
                else:
                    curr_node1 = next_node1
            else:
                # Check if curr_node1 fits between curr_node2 and next_node2
                if not next_node2 or curr_node1.val < next_node2.val:
                    curr_node2.next = curr_node1
                    # FIX: Swap the pointers effectively
                    curr_node2 = curr_node1  # Advance to the connected node
                    curr_node1 = next_node2  # The detached part becomes the other list
                else:
                    curr_node2 = next_node2
                    
        return list1 if list1.val <= list2.val else list2

