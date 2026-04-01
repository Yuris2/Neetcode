import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = {}
        maxHeap = []

        for t in tasks:
            counter[t] = 1 + counter.get(t, 0)
        
        for occ in counter.values():
            maxHeap.append(-occ)
        
        heapq.heapify(maxHeap)
        q = []

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                #Decrement
                count += 1
                #Add if we haven't finished the tasks
                if count != 0:
                    q.append([count, time + n])
            else:
                time = q[0][1]
            
            if q and time == q[0][1]:
                count, time = q.pop(0)
                heapq.heappush(maxHeap, count)
        
        return time

        