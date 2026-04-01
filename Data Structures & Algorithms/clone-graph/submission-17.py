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

        def dfs(n):
            #If we have already seen the node
            if n in oldToNew:
                return oldToNew[n]
            
            copy = Node(n.val)
            oldToNew[n] = copy

            for child in n.neighbors:
                copy.neighbors.append(dfs(child))
            
            return copy
        
        dfs(node)
        return oldToNew[node]




        