import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        time = 0

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        scheduler = []

        for c in counter.values():
            scheduler.append(-c)
        
        heapq.heapify(scheduler)

        cooldown = []
        while scheduler or cooldown:
            time += 1
            if scheduler:
                c = heapq.heappop(scheduler)
                #Decrement
                c += 1
                if c != 0:
                    cooldown.append([c, time + n])
            
            if cooldown and time == cooldown[0][1]:
                heapq.heappush(scheduler, cooldown.pop(0)[0])
        
        return time
        