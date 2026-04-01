class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])

        mergedInterval = [intervals[0]]

        for start, end in intervals:
            if start <= mergedInterval[-1][1]:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], end)
            else:
                mergedInterval.append([start,end])
            
        return mergedInterval
        