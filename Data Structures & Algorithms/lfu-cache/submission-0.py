class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0) # Dummy
        self.tail = Node(0, 0) # Dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_head(self):
        if self.size == 0: return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.index = {} # key: Node
        self.freq_map = {} # freq: DoublyLinkedList
        self.min_freq = 0

    def _update_freq(self, node):
        # Remove from current freq list
        freq = node.freq
        self.freq_map[freq].remove(node)
        
        # If this was the min_freq list and it's now empty, increment min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
            
        # Move to freq + 1 list
        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.index:
            return -1
        node = self.index[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return

        if key in self.index:
            node = self.index[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.index) >= self.cap:
                # Evict the head of the min_freq list (LRU within LFU)
                oldest_node = self.freq_map[self.min_freq].pop_head()
                del self.index[oldest_node.key]
            
            new_node = Node(key, value)
            self.index[key] = new_node
            self.min_freq = 1 # Reset min_freq for a brand new element
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_to_tail(new_node)