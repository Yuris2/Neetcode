class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            comp = target - num

            if comp in dic and dic[comp] != i:
                return [i, dic[comp]]
        
        return [-1,-1]
        