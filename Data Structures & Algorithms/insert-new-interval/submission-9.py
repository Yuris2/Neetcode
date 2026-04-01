class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        idx, n = 0, len(intervals)
        res = []

        while idx < n and intervals[idx][1] < start:
            res.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0] <= end:
            start = min(intervals[idx][0], start)
            end = max(intervals[idx][1], end)

            idx += 1
        
        res.append([start, end])

        while idx < n:
            res.append(intervals[idx])
            idx += 1
        
        return res

        