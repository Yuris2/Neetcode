import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True

        res = dfs(0, -1)
        if len(seen) == n and res:
            return True
        else:
            return False

            
        

            
        

        