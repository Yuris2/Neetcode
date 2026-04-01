from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        common = ctr.most_common(k)
        res = []
        for num, ct in common:
            res.append(num)
        return res