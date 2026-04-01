class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #Key = Key, Value = Node
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    #Helps us insert to front of LL
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        nxt.prev = prev.next = node
        node.prev = prev
        node.next = nxt
    
    #Helps us deleted a node
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            keyNode = self.cache[key]
            cacheVal = keyNode.val
            self.remove(keyNode)
            self.insert(keyNode)
            return cacheVal
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #Updating a value
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        
