import collections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        seen = set()
        
        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                    
        res = 0
        for node in range(n):
            if node not in seen:
                res += 1
                dfs(node)
        
        return res

            
