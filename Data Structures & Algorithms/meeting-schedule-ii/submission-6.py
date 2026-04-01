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
        intervals.sort(key=lambda x:x.start)
        heap = []

        for i in intervals:
            start,end = i.start, i.end

            if heap and start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)
        