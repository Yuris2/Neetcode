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
            return node
        oldToNew = {}
        oldToNew[node] = Node(node.val)

        q = deque([node])

        while q:
            n = q.popleft()

            for neigh in n.neighbors:
                if neigh not in oldToNew:
                    oldToNew[neigh] = Node(neigh.val)
                    q.append(neigh)
                oldToNew[n].neighbors.append(oldToNew[neigh])
        
        return oldToNew[node]



            
