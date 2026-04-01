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
        oldToCopy = {}

        ptr = head

        while ptr:
            copy = Node(ptr.val)
            oldToCopy[ptr] = copy
            ptr = ptr.next
        
        ptr = head

        while ptr:
            copy = oldToCopy[ptr]
            copy.next = oldToCopy.get(ptr.next)
            copy.random = oldToCopy.get(ptr.random)
            ptr = ptr.next
        
        return oldToCopy.get(head)
        