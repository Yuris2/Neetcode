class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        intervals.sort()   
        heap = []     

        qu = [(q,i) for i, q in enumerate(queries)]
        ptr = 0

        for q, i in sorted(qu):
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                l,r = intervals[ptr]
                heapq.heappush(heap, (r - l + 1, r))
                ptr += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]
        
        return res
            
            
