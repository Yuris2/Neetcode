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
        oldToCopy = {None: None}
        ptr = head
        #Duplicating the nodes
        while ptr:
            copy = Node(ptr.val)
            oldToCopy[ptr] = copy
            ptr = ptr.next
            
        
        ptr = head
        while ptr:
            copy = oldToCopy[ptr]
            #Old to copy points to the duplicate.
            copy.next = oldToCopy[ptr.next]
            copy.random = oldToCopy[ptr.random]
            ptr = ptr.next
        
        return oldToCopy[head]
        