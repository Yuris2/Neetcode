class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Map the number to an index
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            c = target - num

            if c in dic and dic[c] != i:
                return [i,dic[c]]
        
        return -1
        