class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            val = node.val
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    
    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = self.right.prev = node
        node.next = self.right
        node.prev = prevNode
    
    def remove(self, node):
        nxtNode, prevNode = node.next, node.prev
        prevNode.next = nxtNode
        nxtNode.prev = prevNode

        
