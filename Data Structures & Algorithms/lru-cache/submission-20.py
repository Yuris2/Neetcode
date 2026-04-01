class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.right.prev = self.left
        self.left.next = self.right
        
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
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def insert(self, node):
        prevNode = self.right.prev
        prevNode.next, self.right.prev = node, node

        node.next = self.right
        node.prev = prevNode

    def remove(self,node):
        prevNode, nxtNode = node.prev, node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode
        
