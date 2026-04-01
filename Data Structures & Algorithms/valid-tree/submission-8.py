import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #A graph is a valid tree if there are no cycles 
        #and every node is reachable
        adjList = defaultdict(list)

        #Construct adjacency list[Undirected]
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        seen = set()
        def dfs(node, prev):
            #Cycle detected
            if node in seen:
                return False
            
            #Add node into set
            seen.add(node)

            #Process children
            for child in adjList[node]:
                #If previous value
                if child == prev:
                    continue
                #Return False up to parent if cycle found
                if not dfs(child, node):
                    return False
            
            return True

        res = dfs(0, -1)
        #If every node is reachable 
        if len(seen) != n or (not res):
            return False
        
        return True
        