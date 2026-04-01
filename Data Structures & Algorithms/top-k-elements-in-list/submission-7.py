class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for key, v in counter.items():
            bucket[v].append(key)
        
        res = []

        for arr in reversed(bucket):
            for n in arr:
                res.append(n)

                if len(res) >= k:
                    return res
        
        return res
        