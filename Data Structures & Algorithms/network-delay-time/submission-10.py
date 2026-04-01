import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], num: int, k: int) -> int:
        adjList = defaultdict(list)

        for n1, n2, w in times:
            adjList[n1].append((n2, w))
        
        seen = set()
        heap = [(0, k)]
        res = 0

        while heap:
            w, n = heapq.heappop(heap)

            if n in seen:
                continue
            
            seen.add(n)
            res = w

            for node, weight in adjList[n]:
                if node not in seen:
                    heapq.heappush(heap, (w + weight, node))
        
        if len(seen) == num:
            return res
        return -1
        
        
        