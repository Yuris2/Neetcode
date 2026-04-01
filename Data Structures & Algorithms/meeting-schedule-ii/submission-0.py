"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import collections
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        heap = []

        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)

        