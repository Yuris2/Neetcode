class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index = count, elts = list(vals) 
        countArr = [[] for _ in range(len(nums) + 1)]

        # val : count
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        
        for val, freq in countMap.items():
            countArr[freq].append(val)
        
        res = []
        for i in range(len(countArr) - 1, -1, -1):
            for val in countArr[i]:
                res.append(val)
                if len(res) == k:
                    return res
        


