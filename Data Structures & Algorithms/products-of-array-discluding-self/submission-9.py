class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        #[1,2,4,6]
        #pre
        #[1,1,2,8]
        #post = 1 * 6 = 6*4 = 24 * 2 = 48
        #[48,24,12,8]

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= post
            post *= nums[i]
        
        return res
        