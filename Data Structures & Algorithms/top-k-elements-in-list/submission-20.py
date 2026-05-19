class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {} # num -> count

        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)
        
        arr = []
        for n, c in numCount.items():
            arr.append([c, n])
        
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
        return res


            