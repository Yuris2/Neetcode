class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal = 0
        intervals.sort()
        
        if not intervals:
            return removal
        
        prevValue = intervals[0][1]

        #[[1, 10], [2, 3], [3, 4]]
        for start, end in intervals[1:]:
            #Non overlapping interval
            if start >= prevValue:
                prevValue = end
            else:
                removal += 1
                prevValue = min(prevValue,end)
        
        return removal

        


        




        