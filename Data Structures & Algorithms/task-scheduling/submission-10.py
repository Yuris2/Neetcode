import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}

        for t in tasks:
            counter[t] = 1 + counter.get(t,0)
        
        cooldown = []
        queue = deque()

        for occ in counter.values():
            cooldown.append(-occ)
        
        heapq.heapify(cooldown)
        time = 0

        while cooldown or queue:
            time += 1
            if cooldown:
                occ = heapq.heappop(cooldown)
                occ += 1

                if occ != 0:
                    queue.append([time + n, occ])

            if queue and queue[0][0] == time:
                t, cnt = queue.popleft()
                heapq.heappush(cooldown, cnt)
        
        return time
                 

        