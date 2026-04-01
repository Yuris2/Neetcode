class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key):
        if key in self.cache:
            keyNode = self.cache[key]
            #Updating to most recently used
            self.remove(keyNode)
            self.insert(keyNode)
            return keyNode.val
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]

    def insert(self, node):
        prevNode = self.right.prev
        self.right.prev = prevNode.next = node

        node.next = self.right
        node.prev = prevNode


    def remove(self, node):
        prevNode = node.prev
        nxtNode = node.next

        prevNode.next = nxtNode
        nxtNode.prev = prevNode


        
