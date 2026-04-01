"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        #Creating a copy
        oldToNew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()

            for n in cur.neighbors:
                #If we don't have a copy of the node
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    queue.append(n)
                oldToNew[cur].neighbors.append(oldToNew[n])
        
        return oldToNew[node]


        