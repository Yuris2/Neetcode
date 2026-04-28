import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for src, dest in tickets:
            heapq.heappush(adjList[src], dest)
        
        res = []

        def dfs(airport):
            while adjList[airport]:
                dest = heapq.heappop(adjList[airport])
                dfs(dest)
            res.append(airport)
        
        dfs("JFK")
        res.reverse()
        return res

        


        