class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        

        l = 0
        r = 0

        while r < len(nums) - 1:
            maxJump = nums[r]

            for i in range(l,r + 1):
                maxJump = max(maxJump, i + nums[i])
            
            l = r + 1
            r = maxJump
            res += 1
        
        return res
        