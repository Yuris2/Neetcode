
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        # count task appearances
            # index = pos in alphabet, val = 
        counts = [0] * 26
        for task in tasks:
            # ascii val - ascii val of A
            counts[(ord(task)) - ord("A")] += 1
        
        # heapify the array
        # max heap, you want to queue the most freq first
        scheduler = [-count for count in counts if count > 0]
        heapq.heapify(scheduler)

        # while there are tasks to take care of
        while scheduler:
            tempq = []
            cycles = n + 1
            while cycles > 0 and scheduler:
                cur = heapq.heappop(scheduler)
                cur += 1
                if cur < 0:
                    tempq.append(cur)
                res += 1
                cycles -= 1

            for task in tempq:
                heapq.heappush(scheduler, task)
            
            if scheduler:
                res += cycles

        return res




