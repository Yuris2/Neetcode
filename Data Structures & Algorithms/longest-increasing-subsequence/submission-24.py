class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[-1] * (n + 1) for _ in range(n + 1)]

        def dp(i, prev):
            if i >= n:
                return 0
            if cache[i][prev] != -1:
                return cache[i][prev]

            res = dp(i + 1, prev)

            if prev == -1 or nums[i] > nums[prev]:
                res = max(res, 1 + dp(i + 1, i))

            cache[i][prev] = res
            return res

        return dp(0, -1)