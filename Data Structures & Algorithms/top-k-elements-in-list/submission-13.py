class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, occ in counter.items():
            buckets[occ].append(num)
        
        res = []

        for bucket in reversed(buckets):
            for item in bucket:
                res.append(item)

                if len(res) == k:
                    return res
        
        