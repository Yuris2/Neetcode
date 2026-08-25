class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        # minHeap
        minHeap = []

        for val, cnt in countMap.items():
            heapq.heappush(minHeap, (cnt, val))
            while len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for i in range(len(minHeap)):
            res.append(heapq.heappop(minHeap)[1])
        
        return res






        