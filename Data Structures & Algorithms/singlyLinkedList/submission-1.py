class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        self.length = 0
    
    def get(self, i):
        if i >= self.length:
            return -1
        
        ptr = self.head.next

        while i > 0:
            ptr = ptr.next
            i -= 1
        
        return ptr.val
    
    def insertHead(self,val):
        nextNode = self.head.next
        newNode = Node(val)

        self.head.next = newNode
        newNode.next = nextNode

        if self.length == 0:
            self.tail = newNode

        self.length += 1
    
    def insertTail(self,val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.length += 1


    def remove(self, i):
        if i >= self.length:
            return False
        
        prevNode = self.head
        count = 0

        while count < i:
            prevNode = prevNode.next
            count += 1
        
        if prevNode.next == self.tail:
            self.tail = prevNode
        
        prevNode.next = prevNode.next.next
        
        self.length -= 1
        return True
    
    def getValues(self):
        res = []
        ptr = self.head.next
        count = 0

        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
            count += 1
        return res


