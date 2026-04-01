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
        rooms = []

        for elem in intervals:
            start, end = elem.start, elem.end

            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, end)
                
        #40, 10, 
        return len(rooms)


        