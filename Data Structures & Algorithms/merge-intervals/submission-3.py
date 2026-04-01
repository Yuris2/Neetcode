class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Sorting interval
        intervals.sort(key=lambda i : i[0])

        mergedInterval = [intervals[0]]

        for start,end in intervals:
            #checking if its within the interval
            if start <= mergedInterval[-1][1]:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], end)
            else:
                #New interval
                mergedInterval.append([start, end])
        
        return mergedInterval

        