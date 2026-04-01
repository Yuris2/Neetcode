import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-freq for freq in counts.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            temp_q = []
            for i in range(n + 1):
                if max_heap:
                    freq = heapq.heappop(max_heap)
                    freq += 1
                    if freq < 0:
                        temp_q.append(freq)
                time += 1
                if not temp_q and not max_heap:
                    break
            for freq in temp_q:
                heapq.heappush(max_heap, freq)
        
        return time

                


        
        

        