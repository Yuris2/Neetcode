import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adjList = defaultdict(list)
        seen = set()
        res = 0

        for src, target, time in times:
            adjList[src].append((target, time))
        
        heap = [[0,k]]

        while heap:
            time , node = heapq.heappop(heap)

            if node in seen:
                continue
            
            seen.add(node)
            res = time

            for child, t in adjList[node]:
                heapq.heappush(heap, (time + t, child))
        
        if len(seen) == n:
            return res
        return -1
            
            
    