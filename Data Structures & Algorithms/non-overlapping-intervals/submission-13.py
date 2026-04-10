class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        
        maxEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= maxEnd:
                maxEnd = end
            else:
                res += 1
                maxEnd = min(maxEnd, end)
        
        return res