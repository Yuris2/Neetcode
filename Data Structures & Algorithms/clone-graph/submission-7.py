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

        queue = deque()

        oldToNew[node] = Node(node.val)
        queue.append(node)

        while queue:
            curr = queue.popleft()

            for child in curr.neighbors:
                if child not in oldToNew:
                    oldToNew[child] = Node(child.val)
                    queue.append(child)
                oldToNew[curr].neighbors.append(oldToNew[child])
        
        return oldToNew[node]



        