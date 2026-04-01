import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        counter = {}
        scheduler = []

        for t in tasks:
            counter[t] = 1 + counter.get(t, 0)
        
        for count in counter.values():
            scheduler.append(-count)
        
        heapq.heapify(scheduler)

        queue = []

        while scheduler or queue:
            res += 1
            if scheduler:
                count = heapq.heappop(scheduler)
                count += 1
                if count != 0:
                    queue.append([count, res + n])

            if queue and queue[0][1] == res:
                heapq.heappush(scheduler, queue.pop(0)[0])     
        
        return res
           

        