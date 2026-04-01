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

        curr = head

        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = oldToCopy[curr]
            copyNode.next = oldToCopy.get(curr.next)
            copyNode.random = oldToCopy.get(curr.random)
            curr = curr.next
        
        return oldToCopy.get(head)
        