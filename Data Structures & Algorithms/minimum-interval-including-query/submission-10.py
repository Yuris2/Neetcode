import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)

        queries = [(q,i) for i,q in enumerate(queries)]
        minH = []
        curr = 0
        #Process Queries in a Sorted Order (tracking their position)
        for q,i in sorted(queries):
            #While the interval is valid (left <= q):
            while curr < len(intervals) and intervals[curr][0] <= q:
                #Add to min heap and check intervals
                l,r = intervals[curr]
                heapq.heappush(minH, (r - l + 1, r))
                curr += 1
            #Remove invalid intervals in heap (right < q)
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            #Top of minHeap will have the answer for given query
            if minH:
                res[i] = minH[0][0]
        
        #Return res
        return res

        