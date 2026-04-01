class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def back(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + back(i + 2), back(i + 1))
            
            return cache[i]
        
        return back(0)
        