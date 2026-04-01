import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for node, target, weight in times:
            adjList[node].append((target,weight))
        
        heap = []
        seen = set()

        heapq.heappush(heap, (0, k))
        res = 0


        while heap:
            weight, node = heapq.heappop(heap)

            if node in seen:
                continue
            
            res = weight
            seen.add(node)

            for target, w in adjList[node]:
                heapq.heappush(heap, (weight + w, target))
        
        if len(seen) == n:
            return res
        else:
            return -1
        


        
        
        