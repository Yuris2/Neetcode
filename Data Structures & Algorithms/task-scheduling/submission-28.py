import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        counts = [0] * 26
        
        for task in tasks:
            counts[ord(task) - ord("A")] += 1
        
        maxHeap = []

        for count in counts:
            if count > 0:
                heapq.heappush(maxHeap, -count)

        while maxHeap:
            tempq = []
            cycles = n + 1
            while cycles > 0 and maxHeap:
                cur = heapq.heappop(maxHeap)
                cur += 1
                if cur < 0:
                    tempq.append(cur)
                res += 1
                cycles -= 1
            
            for task in tempq:
                heapq.heappush(maxHeap, task)
                
            if maxHeap:
                res += cycles

        return res