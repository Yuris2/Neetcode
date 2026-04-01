class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for s,d,w in times:
            adjList[s].append((d,w))
        
        heap = []
        seen = set()
        heapq.heappush(heap, (0, k))
        res = -1

        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
            seen.add(node)

            res = weight
            
            for dest, w in adjList[node]:
                heapq.heappush(heap, (w + weight, dest))
        
        if len(seen) != n:
            return -1
        return res


        