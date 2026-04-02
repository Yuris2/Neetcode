class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # dp[i] will store the length of the LIS ending at index i
        # Every number is an LIS of length 1 by itself
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If current num > previous num, we can extend that sequence
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        