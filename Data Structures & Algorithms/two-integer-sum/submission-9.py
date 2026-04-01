class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for index in range(len(nums)):
            first = nums[index]
            other = target - first
            if other in indexMap:
                return [indexMap[other], index]
            elif first not in indexMap:
                indexMap[first] = index
        