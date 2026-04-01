import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = {}
        maxHeap = []

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        for occ in counter.values():
            maxHeap.append(-occ)
        
        heapq.heapify(maxHeap)
        
        #cooldown
        queue = []

        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                #Decrementing
                count += 1
                if count != 0:
                    #add time and then next time it can be used
                    queue.append([count, time + n])
            else:
                time = queue[0][1]
            
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.pop(0)[0])
        
        return time

        