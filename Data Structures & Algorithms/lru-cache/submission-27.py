class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.cap = capacity

        self.left.next = self.right
        self.right.prev = self.left

        self.cache = {}
        
    def get(self, key: int) -> int:
        val = -1

        if key in self.cache:
            keyNode = self.cache[key]
            val = keyNode.val

            self.remove(keyNode)
            self.insert(keyNode)
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key,value)
        self.cache[key] = newNode

        self.insert(newNode)

        if len(self.cache) > self.cap:
            LRU = self.right.prev
            self.remove(LRU)
            del self.cache[LRU.key]

    
    def insert(self, node):
        nextNode = self.left.next
        node.prev, node.next = self.left, nextNode

        nextNode.prev = node
        self.left.next = node
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
        
