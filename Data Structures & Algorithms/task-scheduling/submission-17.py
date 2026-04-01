import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)

        #Counting occ
        for t in tasks:
            counter[t] += 1
        
        scheduler = []
        
        for occ in counter.values():
            heapq.heappush(scheduler, -occ)
        
        cooldown = deque()

        time = 0
        while scheduler or cooldown:
            if scheduler:
                occ = heapq.heappop(scheduler)
                occ += 1

                if occ != 0:
                    cooldown.append([time + n, occ])
            
            if cooldown and time == cooldown[0][0]:
                cycle, occ = cooldown.popleft()
                heapq.heappush(scheduler, occ)
            
            time += 1
        
        return time

        