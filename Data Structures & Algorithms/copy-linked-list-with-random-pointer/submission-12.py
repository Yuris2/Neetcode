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
        if not head:
            return head
        copyToRandom = {}
        ptr = head

        while ptr:
            copyToRandom[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        
        while ptr:
            copyNode = copyToRandom[ptr]
            copyNode.next = copyToRandom.get(ptr.next, None)
            copyNode.random = copyToRandom.get(ptr.random, None)

            ptr = ptr.next

        return copyToRandom[head]
        