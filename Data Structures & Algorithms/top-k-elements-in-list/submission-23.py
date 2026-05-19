class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        countArr = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            countArr[cnt].append(num)
        
        res = []
        for i in range(len(countArr) - 1, 0, -1):
            for num in countArr[i]:
                res.append(num)
                if len(res) == k:
                    return res
