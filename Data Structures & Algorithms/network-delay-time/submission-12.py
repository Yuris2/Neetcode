import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u,v,t in times:
            adjList[u].append((v,t))
        
        minHeap = [(0, k)]
        seen = set()
        res = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            
            res = time
            seen.add(node)

            for child , t in adjList[node]:
                heapq.heappush(minHeap, (time + t, child))

        if len(seen) == n:
            return res
        return -1
        