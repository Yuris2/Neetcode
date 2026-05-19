class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {} # num -> count

        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)
        
        heap = []
        for n in numCount.keys():
            heapq.heappush(heap, (numCount[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res





            