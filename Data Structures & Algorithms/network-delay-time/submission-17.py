class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for src, dst, t in times:
            adjList[src].append((dst, t))
        
        visit = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            res = time

            for nei, t in adjList[node]:
                heapq.heappush(minHeap, (time + t, nei))
        
        return res if len(visit) == n else -1
            
