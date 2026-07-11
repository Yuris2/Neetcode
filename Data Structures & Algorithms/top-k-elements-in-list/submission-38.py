class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        countMap = {} # val -> count

        for i in range(len(nums)):
            countMap[nums[i]] = 1 + countMap.get(nums[i], 0)

        # array with indices as the count, vals as list of vals
            # size of len(nums) + 1
        
        countArr = [[] for _ in range(len(nums) + 1)]

        for val, cnt in countMap.items():
            countArr[cnt].append(val)
        
        # iterate through countArr lists backwards k times, appending each val to res
        
        for i in range(len(countArr) - 1, 0, -1):
            for val in countArr[i]:
                res.append(val)
                if len(res) == k:
                    return res

