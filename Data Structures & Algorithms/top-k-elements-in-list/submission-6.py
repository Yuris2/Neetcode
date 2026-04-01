class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        #Key = number
        #Value = occurence
        for key, value in counter.items():
            bucket[value].append(key)
        
        res = []

        for b in reversed(bucket):
            for n in b:
                res.append(n)

                if len(res) >= k:
                    return res
        
        return res
        