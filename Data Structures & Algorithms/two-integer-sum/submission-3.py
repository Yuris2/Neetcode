class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = i
        

        for i in range(len(nums)):
            c = target - nums[i]

            if c in dic and dic[c] != i:
                return [i, dic[c]]
        
        return []


        