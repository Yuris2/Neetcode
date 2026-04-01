class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for elem, count in counter.items():
            bucket[count].append(elem)
        
        res = []

        for arr in reversed(bucket):
            for elem in arr:
                res.append(elem)

                if len(res) == k:
                    return res
        
        return res
        