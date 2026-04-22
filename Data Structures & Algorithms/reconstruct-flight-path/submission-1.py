import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adjList = defaultdict(list)

        for start, dest in tickets:
            heapq.heappush(adjList[start], dest)
        
        def dfs(airport):
            while adjList[airport]:
                dest = heapq.heappop(adjList[airport])
                dfs(dest)
            
            res.append(airport)

        dfs("JFK")
        res.reverse()
        return res
        