class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}

        for i,num in enumerate(nums):
            n[num] = i

        for i, num in enumerate(nums):
            comp = target - num

            if comp in n and n[comp] != i:
                return [i,n[comp]]
        
        return []
        