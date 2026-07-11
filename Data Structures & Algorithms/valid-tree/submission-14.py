import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        adjList = defaultdict(list)

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)

            for child in adjList[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        return dfs(0,-1) and len(seen) == n
        