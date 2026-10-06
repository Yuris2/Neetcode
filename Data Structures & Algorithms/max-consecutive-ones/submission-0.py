class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        count = 0
        for num in nums:
            if num == 0:
                max_val = max(max_val, count)
                count = 0
            else:
                count += 1
        return max(max_val, count)

# [1,1,0,1,1,1]
# len = 0, max = 2
