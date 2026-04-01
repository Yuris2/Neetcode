import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        seen = set()

        for n1, n2, w in times:
            adjList[n1].append((n2,w))
        
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, k))

        res = 0
        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
            
            seen.add(node)
            
            res = weight

            for child, w in adjList[node]:
                heapq.heappush(heap, (weight + w, child))

        
        if len(seen) == n:
            return res
        else:
            return -1

            
            

        



        