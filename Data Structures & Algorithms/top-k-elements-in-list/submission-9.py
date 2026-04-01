class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        bucketSort = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            bucketSort[value].append(key)
        
        res = []

        for arr in reversed(bucketSort):
            for num in arr:
                res.append(num)

                if len(res) >= k:
                    return res
        
        return res

        