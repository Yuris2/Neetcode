class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : ListNode
        self.lru = ListNode(0, 0) # head
        self.mru = ListNode(0, 0) # tail
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:       
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value

        else:
            node = ListNode(key, value)
            self.cache[key] = node
        
        self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def insert(self, node): # at mru
        prev, nxt = self.mru.prev, self.mru
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node


    def remove(self, node): 
        prev, nxt = node.prev, node.next
        nxt.prev = prev
        prev.next = nxt

