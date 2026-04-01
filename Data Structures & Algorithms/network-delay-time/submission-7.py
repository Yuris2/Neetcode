import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        res = -1

        for n1, n2, w in times:
            adjList[n1].append([w, n2])
        
        heap = []
        heapq.heappush(heap, (0,k))
        seen = set()

        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
            
            res = weight
            seen.add(node)

            for w, c in adjList[node]:
                heapq.heappush(heap, [weight + w, c])
        
        if len(seen) == n:
            return res
        else:
            return -1
                
            
        


        