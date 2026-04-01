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

        def dfs(n):
            if n in oldToNew:
                return oldToNew[n]
            
            oldToNew[n] = Node(n.val)

            for child in n.neighbors:
                oldToNew[n].neighbors.append(dfs(child))
            
            return oldToNew[n]
        
        dfs(node)
        return oldToNew[node]



        