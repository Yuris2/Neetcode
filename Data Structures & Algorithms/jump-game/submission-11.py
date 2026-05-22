class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        curr = goal

        for n in range(len(nums) - 1, -1, -1):
            if nums[n] + n >= curr:
                curr = n
        
        return curr == 0
        