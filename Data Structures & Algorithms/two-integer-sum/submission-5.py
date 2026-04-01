class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = i
        
        for i in range(len(nums)):
            c = target - nums[i]

            if c in counter and counter[c] != i:
                return [i, counter[c]]
        
        return []
        