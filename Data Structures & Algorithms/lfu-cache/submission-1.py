import collections
class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value

        self.freq = 1

        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.size = 0
        #MFU
        self.left = Node(0,0)
        #LFU
        self.right = Node(0,0)


        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        nextNode = self.left.next
        self.left.next = node
        nextNode.prev = node

        node.next, node.prev = nextNode, self.left

        self.size += 1
    
    def remove(self,node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = None
        node.prev = None

        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0

        #Key:Node
        self.cache = {}
        #Freq:LL
        self.freq = defaultdict(LL)
        
    def get(self, key: int) -> int:
        res = -1

        if key in self.cache:
            node = self.cache[key]
            res = node.val
            self.update(node)
        
        return res
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update(node)
        else:
            #Do we need to evict
            if len(self.cache) == self.cap:
                LFU = self.freq[self.minFreq].right.prev
                self.freq[self.minFreq].remove(LFU)
                del self.cache[LFU.key]
            
            #Insert new key
            node = Node(key,value)
            self.cache[key] = node
            self.freq[1].insert(node)
            self.minFreq = 1

    
    def update(self,node):
        #Update Freq
        oldFreq = node.freq
        self.freq[oldFreq].remove(node)
        
        node.freq += 1
        #See if there is a new minFreq
        if oldFreq == self.minFreq and self.freq[self.minFreq].size == 0:
            #Follow the new node
            self.minFreq += 1
        
        self.freq[node.freq].insert(node)
        



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)