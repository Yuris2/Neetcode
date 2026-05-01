class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        l = 0
        r = 0
        res = 0

        while r < goal:
            maxJump = r

            for j in range(l,r+1):
                maxJump = max(maxJump, j + nums[j])
            
            l = r + 1
            r = maxJump
            res +=1
        
        return res
        