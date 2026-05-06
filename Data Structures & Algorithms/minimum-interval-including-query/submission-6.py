import collections
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        res = [-1] * m

        queries = [(q,i) for i, q in enumerate(queries)]
        minHeap = []
        ptr = 0

        for q,i in sorted(queries):
            while ptr < n and intervals[ptr][0] <= q:
                l,r = intervals[ptr]
                heapq.heappush(minHeap, (r - l + 1, r))
                ptr += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                res[i] = minHeap[0][0]
        
        return res



        