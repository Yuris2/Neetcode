import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Pattern
            #Using a heap to track counts with a cooldown timer
        
        #General Idea
            #Count the occ of each letter, add occ to a max heap
            #Use a queue to mark the next time we can readd to the heap

        count = Counter(tasks)
        scheduler = []
        cooldown = deque()

        for occ in count.values():
            heapq.heappush(scheduler, -occ)
        
        time = 0
        while scheduler or cooldown:
            if scheduler:
                occ = heapq.heappop(scheduler)
                occ += 1

                if occ != 0:
                    cooldown.append((time + n, occ))
            if cooldown and time == cooldown[0][0]:
                t,cycle = cooldown.popleft()
                heapq.heappush(scheduler, cycle)
            time += 1
        
        return time
        

        