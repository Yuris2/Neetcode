class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        
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

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, Node):
        prevNode = Node.prev
        nxtNode = Node.next

        nxtNode.prev = prevNode
        prevNode.next = nxtNode
    
    def insert(self, Node):
        prevNode = self.right.prev
        prevNode.next = Node
        self.right.prev = Node
        Node.prev = prevNode
        Node.next = self.right
        
        
