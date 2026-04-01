import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        scheduler = []

        for occ in counter.values():
            scheduler.append(-occ)
        
        heapq.heapify(scheduler)
        cooldown = []
        time = 0

        while scheduler or cooldown:
            time += 1
            if scheduler:
                occ = heapq.heappop(scheduler)
                occ += 1
                if occ != 0:
                    cooldown.append([time + n, occ])
            
            if cooldown and time == cooldown[0][0]:
                heapq.heappush(scheduler, cooldown.pop(0)[1])

        
        return time


        