import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            weight = values[i]
            #regular edge is normal
            adjList[a].append([b, weight])
            #Reverse edge is the inverse
            adjList[b].append([a, 1/ weight])
        
        def bfs(num, denom):
            if num not in adjList or denom not in adjList:
                return -1
            
            q = deque()
            seen = set()

            q.append([num, 1])
            seen.add(num)

            while q:
                for _ in range(len(q)):
                    node, weight = q.popleft()

                    if node == denom:
                        return weight

                    for adj, outWeight in adjList[node]:
                        if adj not in seen:
                            q.append([adj, weight * outWeight])
                            seen.add(adj)
            
            return -1

        res = []
        for num, denom in queries:
            res.append(bfs(num, denom))
        return res

        