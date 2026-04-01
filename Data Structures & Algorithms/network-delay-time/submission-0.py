import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        adjList = defaultdict(list)
        #Constructing adjacency list
        for u,v,w in times:
            adjList[u].append((v,w))

        seen = set()  
        heap = [(0,k)]
        heapq.heapify(heap)

        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue 
            time = weight
            seen.add(node)

            for child, w in adjList[node]:
                if child not in seen:
                    heapq.heappush(heap, (w + weight, child))
        
        if len(seen) == n:
            return time
        else:
            return -1

        


        