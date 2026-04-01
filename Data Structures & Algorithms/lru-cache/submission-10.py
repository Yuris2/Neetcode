class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            keyNode = self.cache[key]
            val = keyNode.val
            #Update to most freq
            self.remove(keyNode)
            self.insert(keyNode)
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    
    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = self.right.prev = node
        node.prev = prevNode
        node.next = self.right
    
    def remove(self, node):
        prevNode = node.prev
        nxtNode = node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode

        
