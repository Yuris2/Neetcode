import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for src, dest in tickets:
            heapq.heappush(adjList[src], dest)
        
        res = []

        def dfs(src):
            while adjList[src]:
                dest = heapq.heappop(adjList[src])
                dfs(dest)
            res.append(src)
        
        dfs("JFK")
        res.reverse()
        return res

        