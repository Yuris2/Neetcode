class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        #Work from right to left
        for i in range(len(nums) - 1, -1, -1):
            #Check all j > i
            for j in range(i + 1, len(nums)):
                #Do we get a better res from extending?
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

