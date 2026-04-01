import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        scheduler = []
        counter = {}
        time = 0

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        for occ in counter.values():
            scheduler.append(-occ)

        heapq.heapify(scheduler)
        cooldown = []
        
        while scheduler or cooldown:
            time += 1
            if scheduler:
                value = heapq.heappop(scheduler)
                value += 1

                if value != 0:
                    cooldown.append([time + n, value])

            if cooldown and time == cooldown[0][0]:
                t, occ = cooldown.pop(0)
                heapq.heappush(scheduler, occ)
        
        return time
        


        