import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i in range(len(equations)):
            num, denom = equations[i]
            value = values[i]

            #a -> b[weight]
            adjList[num].append([denom, value])
            adjList[denom].append([num, 1 / value])

        def bfs(num,denom):
            if num not in adjList or denom not in adjList:
                return -1

            queue = deque()
            seen = set()

            queue.append([num, 1])
            seen.add(num)

            while queue:
                for _ in range(len(queue)):
                    node, weight = queue.popleft()

                    if node == denom:
                        return weight
                    for adj, edgeW in adjList[node]:
                        if adj not in seen:
                            queue.append([adj, weight * edgeW])
                            seen.add(adj)
            
            return -1

        res = []
        for num,denom in queries:
            res.append(bfs(num, denom))
        return res

        