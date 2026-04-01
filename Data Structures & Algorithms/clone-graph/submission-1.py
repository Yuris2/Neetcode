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
        #We are checking if the old value already has a copy
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()

            for neighbor in cur.neighbors:
                #If we haven't previously visisted the node
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                #Get the copy of popped left and then get copy of neighbor
                oldToNew[cur].neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]


        