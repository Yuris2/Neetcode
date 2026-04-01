class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)

        bucketArr = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            bucketArr[value].append(key)

        topK = []

        for bucket in reversed(bucketArr):
            for n in bucket:
                topK.append(n)

                if len(topK) == k:
                    return topK
                

        return topK



        