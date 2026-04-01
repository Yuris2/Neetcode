class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            cur = nums[i]
            diff = target - cur
            if diff in numDict:
                return [numDict[diff], i]
            else:
                numDict[cur] = i