import collections
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)
        minHeap = []
        ptr = 0

        #Changing queries so we can also track the index
        queries = [(q,i) for i,q in enumerate(queries)]

        for q, idx in sorted(queries):
            #Adding relevant queries to the heap
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                l,r = intervals[ptr]
                heapq.heappush(minHeap,(r - l + 1, r))
                ptr += 1
            #Removing irrelevant queries from heap
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                res[idx] = minHeap[0][0]
        
        return res
        