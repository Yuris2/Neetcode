class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}        
        #Most FREQ
        self.right = Node(0,0)
        self.left = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        nodeVal = -1
        if key in self.cache:
            nodeVal = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        
        return nodeVal

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next = self.right.prev = node
        
        node.prev = prevNode
        node.next = self.right
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        nextNode.prev = prevNode
        prevNode.next = nextNode
        
