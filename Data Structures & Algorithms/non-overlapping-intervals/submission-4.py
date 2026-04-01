class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        #Set prevEnd at first end
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            #If new start has no overlap
            if start >= prevEnd:
                prevEnd = end
            else:
                #We have to remove and interval
                res +=1
                #We want to remove the interval
                #with last end (longest interval)
                prevEnd = min(prevEnd, end)
        
        return res
        