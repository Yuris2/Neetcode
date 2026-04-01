class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        buckets = [[] for i in range(len(nums) + 1)]
        for num, occ in counter.items():
            buckets[occ].append(num)
        
        res = []
        for bucket in reversed(buckets):
            for elt in bucket:
                res.append(elt)
                if len(res) == k:
                    return res