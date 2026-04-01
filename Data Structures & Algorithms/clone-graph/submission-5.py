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

        queue = deque()
        queue.append(node)

        while queue:
            cur = queue.popleft()

            for n in cur.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    queue.append(n)
                oldToNew[cur].neighbors.append(oldToNew[n])
        
        return oldToNew[node]
        