import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t,0)
        
        scheduler = []
        for occ in count.values():
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
            else:
                time == cooldown[0][0]
            if cooldown and time == cooldown[0][0]:
                heapq.heappush(scheduler, cooldown.pop(0)[1])
        
        return time
            

        