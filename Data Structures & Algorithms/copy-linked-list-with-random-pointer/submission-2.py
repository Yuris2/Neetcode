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
        #2 Pass Approach
        oldToCopy = {None: None}
        #Creating a copy of each node and mapping oldVal to Copy
        cur = head
        while cur:
            #Copying the value
            copy = Node(cur.val)
            #Mapping old value to copy
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            #Retrieivng the deep copy
            copy = oldToCopy[cur]
            #Filling copy.next
            copy.next = oldToCopy[cur.next]
            #Filling copy.random
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]
        
        
        