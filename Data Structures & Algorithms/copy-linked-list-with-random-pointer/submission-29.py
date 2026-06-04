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
        oldToNew = defaultdict(lambda: Node(0))
        oldToNew[None] = None
        
        cur = head

        while cur:
            oldToNew[cur].val = cur.val
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]








