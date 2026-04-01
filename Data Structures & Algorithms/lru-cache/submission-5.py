class Node:
    def __init__ (self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #LRU
        self.left = Node(0,0)
        #Most recent
        self.right = Node(0,0)
        #Initialize
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        
        return val
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        newNode = self.cache[key] = Node(key, value)
        self.insert(newNode)

        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]


    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = self.right.prev = node
        node.next = self.right
        node.prev = prevNode
    
    def remove(self, node):
        nxtNode = node.next
        prevNode = node.prev
        prevNode.next = nxtNode
        nxtNode.prev = prevNode
        
