import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            weight = values[i]

            adjList[a].append([b,weight])
            adjList[b].append([a, 1/ weight])
        
        
        def bfs(num, denom):
            if num not in adjList or denom not in adjList:
                return -1
            
            queue = deque()
            seen = set()
            queue.append([num, 1])
            seen.add(num)
            

            while queue:
                for _ in range(len(queue)):
                    node, w = queue.popleft()

                    if node == denom:
                        return w

                    for child, weight in adjList[node]:
                        if child not in seen:
                            queue.append([child, weight * w])
                            seen.add(child)
            
            return -1

        res = []
        for num, denom in queries:
            res.append(bfs(num, denom))
        
        return res
        