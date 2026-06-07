class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Pattern:
            #1D-DP to find consecutive increasing elements
        
        #General Idea
            #Set up dp table w/ 1's corresponding to longest subsequence from index
            #Iterate through the array backwords (j)
            #Iterate through numbers starting from j till end of arrray
                #If nums[i] > nums[j], dp[j] = max(dp[j], dp[i])
            #Find the max length from dp array
        n = len(nums)
        dp = [1] * n

        for j in range(n - 1, -1, -1):
            for i in range(j + 1, n):
                if nums[i] > nums[j]:
                    dp[j] = max(dp[j], 1 + dp[i])
        
        return max(dp)
        



        