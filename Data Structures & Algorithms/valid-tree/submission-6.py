import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        seen = set()

        def dfs(node, prevValue):
            if node in seen:
                return False
            
            seen.add(node)

            for child in adjList[node]:
                if child == prevValue:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        res = dfs(0,-1)

        if len(seen) != n:
            return False
        return res

        