class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        res = 0

        l = 0
        r = 0

        while r < goal:
            maxJump = nums[r]

            for j in range(l,r + 1):
                maxJump = max(maxJump, nums[j] + j)
            
            l = r + 1
            r = maxJump    
            res += 1
        
        return res
        