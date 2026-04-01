class Solution:
    def numDecodings(self, nums: str) -> int:
        end = {'0', '1', '2', '3', '4', '5', '6'}
        cache = {}
        #Deal with leading 0's
        def back(i):
            if i >= len(nums):
                return 1
            if nums[i] == '0':
                return 0
            if i in cache:
                return cache[i]
            
            #Single digit numbers
            res = back(i + 1)

            #Valid double digits
            if i < len(nums) - 1:
                if nums[i] == '1' or (nums[i] == '2' and nums[i + 1] in end):
                    res += back(i + 2)
            
            cache[i] = res
            return res
        
        return back(0)

            

        