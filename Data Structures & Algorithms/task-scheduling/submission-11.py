import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        scheduler = []
        cooldown = deque()

        for occ in counter.values():
            scheduler.append(-occ)
        heapq.heapify(scheduler)
        
        time = 0
        while scheduler or cooldown:
            if scheduler:
                time += 1
                occ = heapq.heappop(scheduler)
                occ += 1

                if occ != 0:
                    cooldown.append([time + n, occ])
            else:
                time = cooldown[0][0]
            if cooldown and cooldown[0][0] == time:
                t, cnt = cooldown.popleft()
                heapq.heappush(scheduler, cnt)
        
        return time
