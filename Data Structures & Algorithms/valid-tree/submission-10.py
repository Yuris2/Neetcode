import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #All nodes have to be connected
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            
            for child in adjList[node]:
                #Previous Child
                if child == prev:
                    continue
                #IF we have found a cycle anywhere
                if not dfs(child, node):
                    return False
            #NO cycles
            return True
        
        res = dfs(0, -1)

        if len(seen) != n:
            return False
        return res
        






        