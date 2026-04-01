import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for n1,n2,weight in times:
            adjList[n1].append((n2, weight))
        
        heap = [(0,k)]
        heapq.heapify(heap)
        seen = set()

        res = 0

        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
            
            seen.add(node)
            res = weight

            for child, w in adjList[node]:
                heapq.heappush(heap, (w + weight, child))
        
        if len(seen) != n:
            return -1
        return res




        