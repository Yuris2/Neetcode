class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {} # num -> count

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        
        countArr = [[] for i in range(len(nums) + 1)]
        for num, cnt in countMap.items():
            countArr[cnt].append(num)
        
        res = []

        for i in range(len(countArr) - 1, 0, -1):
            for n in countArr[i]:
                res.append(n)
                if len(res) == k:
                    return res



