import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for n1, n2, weight in times:
            adjList[n1].append([n2, weight])
        
        heap = []
        heapq.heappush(heap, (0, k))
        seen = set()
        res = -1

        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
                
            res = weight
            seen.add(node)
            for child, w in adjList[node]:
                heapq.heappush(heap, [weight + w, child])
        
        if len(seen) == n:
            return res
        else:
            return -1
        
        