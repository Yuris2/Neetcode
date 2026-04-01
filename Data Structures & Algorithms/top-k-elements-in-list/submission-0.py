class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            bucket[value].append(key)

        topK = []

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                topK.append(n)
                if len(topK) == k:
                    return topK
        
        return topK


        