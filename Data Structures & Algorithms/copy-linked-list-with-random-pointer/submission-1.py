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
        oldToHead = {None: None}

        cur = head

        while cur:
            newNode = Node(cur.val)
            oldToHead[cur] = newNode
            cur = cur.next
        
        cur = head
        
        while cur:
            newNode = oldToHead[cur]
            newNode.next = oldToHead[cur.next]
            newNode.random = oldToHead[cur.random]
            cur = cur.next
        
        return oldToHead[head]
        