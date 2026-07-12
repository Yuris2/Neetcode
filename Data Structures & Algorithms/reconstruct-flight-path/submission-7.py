import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adjList = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adjList[src], dst)
        

        def dfs(airport):
            while adjList[airport]:
                dest = heapq.heappop(adjList[airport])
                dfs(dest)
            res.append(airport)
        
        dfs("JFK")
        res.reverse()
        return res


        