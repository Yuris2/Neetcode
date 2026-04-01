import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        
        maxHeap = []

        for occ in counter.values():
            heapq.heappush(maxHeap, -occ)
        
        cooldown = deque()
        time = 0
 
        while maxHeap or cooldown:
            if maxHeap:
                occ = heapq.heappop(maxHeap)
                occ += 1

                if occ != 0:
                    cooldown.append([occ, time + n])
            if cooldown and time == cooldown[0][1]:
                occ, t = cooldown.popleft()
                heapq.heappush(maxHeap, occ)
            time += 1
        
        return time
        


        