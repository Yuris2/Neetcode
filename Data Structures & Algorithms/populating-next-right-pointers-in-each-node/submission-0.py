"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        #Keep track of current level
        cur = root
        #Keep track of next level
        nxt = root.left

        #Populate the next pointers from the level above
        while cur and nxt:
            #Connecting l -> r
            cur.left.next = cur.right

            #If there exists a neighboring subtree
            if cur.next:
                cur.right.next = cur.next.left
            
            cur = cur.next

            #If there are no more children go to next level
            if not cur:
                cur = nxt
                nxt = cur.left
        
        return root


        