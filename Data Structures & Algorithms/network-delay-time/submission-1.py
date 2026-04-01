import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for n1,n2,w in times:
            adjList[n1].append((n2, w))
        
        seen = set()
        heap = [(0, k)]
        heapq.heapify(heap)

        res = 0
        while heap:
            w, node = heapq.heappop(heap)

            if node in seen:
                continue 
                
            seen.add(node)

            res = w

            for child, weight in adjList[node]:
                if child not in seen:
                    heapq.heappush(heap, (w + weight, child))
        
        if len(seen) != n:
            return -1
        else:
            return res







        