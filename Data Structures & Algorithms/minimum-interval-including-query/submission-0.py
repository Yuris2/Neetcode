class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #Given a list of intervals and query points
        #Return a list of integers where
            #res[i] = shortest interval that contains query[i]
                #res[i] = -1 if query is not contained
        
        res = [-1] * len(queries)
        intervals.sort()
        #Holds intervals that are currenly active
        minHeap = []

        #Point to sorted intervals
        ptr = 0
        queries = [(q,i) for i,q in enumerate(queries)]
        #Sort by both queries and intervals
        for q,i in sorted(queries):
            #Add relevant queries to the heap
            while ptr < len(intervals) and intervals[ptr][0] <= q:
                left, right = intervals[ptr]
                heapq.heappush(minHeap, (right - left + 1, right))
                ptr += 1
            #Remove irrelevant queries from heap
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            #If there is a valid interval
            if minHeap:
                res[i] = minHeap[0][0]
        
        return res


        