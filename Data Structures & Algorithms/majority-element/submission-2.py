class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        res = maxCount = 0

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
            if maxCount < countMap[num]:
                res = num
                maxCount = countMap[num]
        
        return res

            
