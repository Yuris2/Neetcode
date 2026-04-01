class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for number, occ in counter.items():
            bucket[occ].append(number)
        
        res = []
        for b in reversed(bucket):
            for elem in b:
                res.append(elem)

                if len(res) == k:
                    return res

        