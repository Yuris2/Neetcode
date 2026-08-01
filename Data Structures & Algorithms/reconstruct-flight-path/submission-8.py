import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adjList[src], dst)
        
        res = []

        def dfs(airport):
            while adjList[airport]:
                dst = heapq.heappop(adjList[airport])
                dfs(dst)
            
            res.append(airport)

            return
        
        dfs("JFK")
        res.reverse()
        return res



        