class Node:
    def __init__(self, val, key):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.mapper = dict()
        self.capacity = capacity
        self.current_capacity = 0
        self.dll = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.mapper:
            return -1
        node = self.mapper[key]
        if node == self.dll: #node trying to access is already in head position, no need to update pos
            return node.val
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        if node != self.tail:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        self.dll.prev = node
        node.next = self.dll
        node.prev = None
        self.dll = node
        return node.val

    def put(self, key: int, value: int) -> None:
        #existing key
         #node we're trying to update is head So no position update is required
         #node is not head So the node we're trying to update should be moved to head
         #no change in mapper
        if key in self.mapper:
            node = self.mapper[key]
            if node == self.dll:
                self.dll.val = value
            else:
                node.val = value
                prev_node = node.prev
                next_node = node.next #this can be None
                prev_node.next = next_node
                if node != self.tail:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                self.dll.prev = node
                node.next = self.dll
                node.prev = None
                self.dll = node
        else:
            # create new node
            new_node = Node(value, key)
             # capacity is full So need to delete tail node and insert new one at the head
                # delete tail node, prev node becomes tail node
            if self.current_capacity >= self.capacity:
                if self.dll == self.tail:
                    del self.mapper[self.dll.key]
                    self.dll = new_node
                    self.tail = new_node
                    self.mapper[key] = new_node
                else:
                    prev_node = self.tail.prev
                    prev_node.next = None
                    del self.mapper[self.tail.key]
                    self.tail = prev_node
                    self.dll.prev = new_node
                    new_node.next = self.dll
                    self.mapper[key] = new_node
                    self.dll = new_node
            else:
                self.current_capacity += 1
                if not self.dll:
                    self.dll = new_node
                    self.tail = new_node
                    self.mapper[key] = new_node
                    return
                self.dll.prev = new_node
                new_node.next = self.dll
                self.mapper[key] = new_node
                self.dll = new_node
        
