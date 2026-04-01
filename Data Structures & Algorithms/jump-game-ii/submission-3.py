class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        goal = len(nums) - 1

        while r < len(nums) - 1:
            maxJump = 0
            for j in range(l,r+1):
                maxJump = max(maxJump, j + nums[j])
            
            l = r + 1
            r = maxJump
            res += 1
        
        return res

        