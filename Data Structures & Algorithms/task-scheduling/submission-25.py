import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        time = 0
        cooldown = deque()
        scheduler = []

        for occ in count.values():
            heapq.heappush(scheduler, -occ)
        
        while scheduler or cooldown:
            time += 1
            if scheduler:
                cycle = heapq.heappop(scheduler)
                cycle += 1

                if cycle != 0:
                    cooldown.append((time + n, cycle))

            if cooldown and cooldown[0][0] == time:
                _, cycle = cooldown.popleft()
                heapq.heappush(scheduler, cycle)
        
        return time


        
