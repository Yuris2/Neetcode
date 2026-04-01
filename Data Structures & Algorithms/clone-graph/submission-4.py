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
        queue = deque()

        queue.append(node)
        oldToNew[node] = Node(node.val)
        
        while queue:
            for i in range(len(queue)):
                oldNode = queue.popleft()

                for n in oldNode.neighbors:
                    if n not in oldToNew:
                        oldToNew[n] = Node(n.val)
                        queue.append(n)
                    oldToNew[oldNode].neighbors.append(oldToNew[n])
        
        return oldToNew[node]
        
        
        