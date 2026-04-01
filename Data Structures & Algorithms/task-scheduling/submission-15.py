import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        scheduler = []
        cooldown = []
        cycles = 0

        for occ in counter.values():
            heapq.heappush(scheduler, -occ)
        
        while scheduler or cooldown:
            cycles += 1
            if scheduler:
                occ = heapq.heappop(scheduler)
                occ += 1

                if occ != 0:
                    cooldown.append((cycles + n, occ))
            
            if cooldown and cycles == cooldown[0][0]:
                time, occ = cooldown.pop(0)
                heapq.heappush(scheduler, occ)
        
        return cycles

        