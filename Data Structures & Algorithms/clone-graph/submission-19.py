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
        
        oldToNew = {node: Node(node.val)}
        q = deque([node])

        while q:
            n = q.popleft()

            for child in n.neighbors:
                if child not in oldToNew:
                    oldToNew[child] = Node(child.val)
                    q.append(child)
                oldToNew[n].neighbors.append(oldToNew[child])
        
        return oldToNew[node]
            


        