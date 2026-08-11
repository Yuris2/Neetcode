class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> ListNode
        # DLL: left -> LRU, right -> MRU
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
    # read val from key -> ListNode
        if key in self.cache:
            node = self.cache[key]
            # remove old node and insert new node DLL MRU side
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key already exists 
        if key in self.cache:
            # remove the old node from DLL
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        node = self.cache[key]
        self.insert(node)

        while len(self.cache) > self.capacity:
            # remove lru (key, val) from cache and DLL
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): # at right
        prev, nxt = self.right.prev, self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node

