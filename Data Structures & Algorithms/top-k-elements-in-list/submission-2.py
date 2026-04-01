class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        bucketArr = [[] for i in range(len(nums) + 1)]

        for num, occ in counter.items():
            bucketArr[occ].append(num)
        
        topK = []

        for bucket in reversed(bucketArr):
            for n in bucket:
                topK.append(n)

                if len(topK) == k:
                    return topK
        
        