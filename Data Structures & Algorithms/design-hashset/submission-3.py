class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
class MyHashSet:

    def __init__(self):
        self.hashtable = [Node(-1) for _ in range(10000)]
    
    def hashkey(self, val):
        return val % len(self.hashtable)

    def add(self, key: int) -> None:
        hashkey = self.hashkey(key)
        ptr = self.hashtable[hashkey]

        while ptr.next:
            if ptr.next.key == key:
                return
            ptr = ptr.next

        ptr.next = Node(key)
        
    def remove(self, key: int) -> None:
        hashkey = self.hashkey(key)

        ptr = self.hashtable[hashkey]

        while ptr.next and ptr.next.key != key:
            ptr = ptr.next

        if ptr.next:
            ptr.next = ptr.next.next
        else:
            ptr.next = None

    def contains(self, key: int) -> bool:
        hashkey = self.hashkey(key)

        ptr = self.hashtable[hashkey]

        while ptr:
            if ptr.key == key:
                return True
            ptr = ptr.next
        
        return False
            


    
    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)