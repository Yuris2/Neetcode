class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum = 1
        maximum = 1
        res = -2e9

        for n in nums:
            temp = minimum
            minimum = min(minimum * n, n, maximum * n)
            maximum = max(maximum * n, temp * n, n)

            res = max(res, maximum)
        
        return res


            
        