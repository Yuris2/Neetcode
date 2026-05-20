class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        m = len(intervals)
        intervals.sort()
        ptr = 0
        res = [-1] * n

        queries = [(q,i) for i,q in enumerate(queries)]

        heap = []

        for q,i in sorted(queries):
            while ptr < m and intervals[ptr][0] <= q:
                l,r = intervals[ptr]
                heapq.heappush(heap, (r - l + 1, r))
                ptr += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]
        
        return res
        