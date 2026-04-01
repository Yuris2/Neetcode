import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = []

        counter = {}
        for t in tasks:
            counter[t] = 1 + counter.get(t, 0)
        
        maxHeap = []
        for m in counter.values():
            maxHeap.append(-m)
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count != 0:
                    q.append([count, time + n])
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.pop(0)[0])
        
        return time


        