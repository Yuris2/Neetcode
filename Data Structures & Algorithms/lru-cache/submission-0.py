class Node:
    #Key, Value, Prev, Next
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #Intialize 2 Dummy Nodes
        self.left = Node(0, 0)
        #Most used element are on the rightmost side
        self.right = Node(0,0)
        #Assign dummy Nodes to point at each other
        self.left.next = self.right
        self.right.prev = self.left
    
    #Remove
    # - void method
    # - removes a node from the cache specified at node
    # - (node type) = Doubly LL or Node()
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        #Changing pointers to skip over current node
        prev.next = nxt
        nxt.prev = prev

    #Insert
    # - void method
    # - adds a node to the right end of a Double LL or Node()
    # - (node type) = Doubly LL or Node()
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        node.prev = prev
        node.next = nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            keyNode = self.cache[key]
            cacheVal = keyNode.val
            self.remove(keyNode)
            self.insert(keyNode)
            return cacheVal
        
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
        
