class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        #Dummy Nodes
        self.left = Node(0,0)
        self.right = Node(0,0)
        #Initialzing Dummy Nodes
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = next.prev = node
        node.next = next
        node.prev = prev
    
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            Node = self.cache[key]

            self.remove(Node)
            self.insert(Node)

            return Node.value
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
        
        

        
