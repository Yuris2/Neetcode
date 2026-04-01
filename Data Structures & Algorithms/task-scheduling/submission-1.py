class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for c in tasks:
            counter[c] = 1 + counter.get(c,0)
        
        maxHeap = []
        for occ in counter.values():
            maxHeap.append(-occ)
        
        heapq.heapify(maxHeap)

        time = 0
        q = []

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
            
                

        
        