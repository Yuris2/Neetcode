class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class MyHashMap:
    def __init__(self):
        self.bucket = [Node(-1, -1) for _ in range(1000)]

    def index(self, key):
        return hash(key) % len(self.bucket)

    def put(self, key, value):
        dummy = self.bucket[self.index(key)]
        curr = dummy.next

        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next

        new_node = Node(key, value)
        new_node.next = dummy.next
        new_node.prev = dummy

        if dummy.next:
            dummy.next.prev = new_node

        dummy.next = new_node

    def get(self, key):
        curr = self.bucket[self.index(key)].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1

    def remove(self, key):
        curr = self.bucket[self.index(key)].next

        while curr:
            if curr.key == key:
                self.removeNode(curr)
                return
            curr = curr.next

    def removeNode(self, node):
        node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev