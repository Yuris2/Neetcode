import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #We have a list of plane tickets [src, dest] and we want to construct it s.t 
        #we have a single flight path which combines all tickets
            #They always start at JFK
            # If there is a tie
                #Choose the path that is first alphabetically
        
        #Eulerian Path: Visit Every Edge, 
        #Algorithm:
            #Run DFS on every node:
                #If node has no children, add to front of result and back
                #If node has children, take DFS down the path and continue
        
        #Application for Our Problem
            #Use a heap to track lexographically smallest edge 
            #No children = empty heap
        
        adjList = defaultdict(list)

        #Construct adj list
        for src, dst in tickets:
            heapq.heappush(adjList[src], dst)
        
        res = []

        def dfs(airport):
            #Keep going down until the heap has values
            while adjList[airport]:
                #Get smallest airport
                dst = heapq.heappop(adjList[airport])
                #Go down that path
                dfs(dst)
            
            #No more outbound edges, we can add to res and backtrack
            res.append(airport)

            return
        
        #Starting airport
        dfs("JFK")

        res.reverse()
        return res

        