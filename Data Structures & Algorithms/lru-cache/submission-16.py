class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            keyNode = self.cache[key]
            val = keyNode.value
            self.remove(keyNode)
            self.insert(keyNode)
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def remove(self, node):
        nxtNode = node.next
        prevNode = node.prev

        prevNode.next = nxtNode
        nxtNode.prev = prevNode
    
    def insert(self,node):
        prevNode = self.right.prev
        prevNode.next = node
        self.right.prev = node

        node.next, node.prev = self.right, prevNode

        
