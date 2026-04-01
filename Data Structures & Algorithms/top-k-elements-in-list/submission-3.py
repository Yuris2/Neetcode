class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        #Bucket
        bucket = [[] for n in range(len(nums) + 1)]

        for key,value in counter.items():
            bucket[value].append(key)
        
        topK = []

        for arr in reversed(bucket):
            for element in arr:
                topK.append(element)

                if len(topK) == k:
                    return topK
        
        return topK

        