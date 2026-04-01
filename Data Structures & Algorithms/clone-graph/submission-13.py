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
        
        oldToCopy = {}
        oldToCopy[node] = Node(node.val)
        queue = deque([node])

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in oldToCopy:
                    oldToCopy[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToCopy[n].neighbors.append(oldToCopy[neighbor])

        return oldToCopy[node]                
        