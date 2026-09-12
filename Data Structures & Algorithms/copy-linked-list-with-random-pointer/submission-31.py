"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        oldToNew = {None:None}

        while ptr:
            node = Node(ptr.val)
            oldToNew[ptr] = node
            ptr = ptr.next
        
        ptr = head
        while ptr:
            oldToNew[ptr].next = oldToNew[ptr.next]
            oldToNew[ptr].random = oldToNew[ptr.random]
            ptr = ptr.next
        
        return oldToNew[head]
        