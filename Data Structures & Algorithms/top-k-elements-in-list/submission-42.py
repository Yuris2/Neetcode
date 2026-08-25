class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {} # val : freq
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        # countArr of len(nums) + 1
        # i = freq, val = list of nums
        countArr = [[] for _ in range(len(nums) + 1)]
        for n in countMap:
            countArr[countMap[n]].append(n)

        res = []
        for i in range(len(countArr) - 1, -1, -1):
            for n in countArr[i]:
                res.append(n)
                if len(res) == k:
                    return res






        