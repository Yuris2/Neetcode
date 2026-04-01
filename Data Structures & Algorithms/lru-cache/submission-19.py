class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

#Essentially, key, value pair of doubly linkedlist. Use a dictionary to map key:Node. Main reason for doubly linkedlist is for easier 
#shifting of elements
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
            keyNode = self.cache[key]
            val = keyNode.val
            self.remove(keyNode)
            self.add(keyNode)
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.add(newNode)

        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def add(self, node):
        prevNode = self.right.prev
        
        prevNode.next = node
        self.right.prev = node

        node.prev = prevNode
        node.next = self.right
    
    def remove(self,node):
        prevNode, nxtNode = node.prev, node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode

        
