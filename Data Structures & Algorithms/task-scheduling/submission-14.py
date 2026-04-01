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
            if scheduler:
                value = heapq.heappop(scheduler)
                value += 1

                if value != 0:
                    cooldown.append([cycles + n, value])
            if cooldown and cooldown[0][0] == cycles:
                time, value = cooldown.pop(0)
                heapq.heappush(scheduler, value)
            cycles += 1
        
        return cycles

        