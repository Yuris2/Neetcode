class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for index in range(len(nums)):
            first = nums[index]
            diff = target - first
            if diff in indexMap:
                return [indexMap[diff], index]
            else:
                indexMap[first] = index
        