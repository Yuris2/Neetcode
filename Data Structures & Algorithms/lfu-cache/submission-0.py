import collections
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.size = 0

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        nextNode = self.left.next
        nextNode.prev = node
        node.next = nextNode
        node.prev = self.left
        self.left.next = node

        self.size += 1
    
    def remove(self, node):
        prevNode,nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = None
        node.prev = None

        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        #Key:Node
        self.cache = {}
        #Freq: Nodes at That Freq
        self.freq = defaultdict(LL)
        #Min Freq
        self.minFreq = 0
        
    def get(self, key: int) -> int:
        res = -1

        if key in self.cache:
            keyNode = self.cache[key]
            res = keyNode.value
            self.updateFreq(keyNode)

        return res

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            keyNode = self.cache[key]
            keyNode.value = value
            self.updateFreq(keyNode)
        else:
            #Evict from LFU
            if len(self.cache) == self.cap:
                LFU = self.freq[self.minFreq].right.prev
                self.freq[self.minFreq].remove(LFU)
                del self.cache[LFU.key]

            self.cache[key] = Node(key,value)
            self.cache[key].freq = 1

            self.freq[1].insert(self.cache[key])

            self.minFreq = 1

    
    def updateFreq(self, keyNode):
        oldFreq = keyNode.freq

        #Remove from LL
        self.freq[oldFreq].remove(keyNode)
        #Update min freq
        if oldFreq == self.minFreq and self.freq[oldFreq].size == 0:
            self.minFreq += 1
        #Increment
        keyNode.freq += 1
        #Add to the next LL
        self.freq[keyNode.freq].insert(keyNode)

        return



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)