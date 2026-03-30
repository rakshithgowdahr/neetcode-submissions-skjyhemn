"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = dict()
        index = 0
        c_node = head
        new_ll = Node(0)
        nc_node = new_ll
        while c_node:
            new_node = Node(c_node.val)
            nc_node.next = new_node
            nc_node = nc_node.next
            hash_map[index] = {"old": None, "new": None}
            hash_map[index]["old"] = c_node
            hash_map[index]["new"] = nc_node
            index += 1
            c_node = c_node.next
        for key in hash_map:
            main_node = hash_map[key]["old"]
            for s_key in hash_map:
                loop_node = hash_map[s_key]["old"]
                if loop_node.random == main_node:
                    hash_map[s_key]["new"].random = hash_map[key]["new"]
        return new_ll.next