class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        
        if summation % 2 != 0:
            return False
        
        cache = {}
        target = summation // 2

        def dfs(i, acc):
            if acc == target:
                return True
            if (i, acc) in cache:
                return cache[(i,acc)]
            
            if acc > target or i >= len(nums):
                return False
            
            res =  dfs(i + 1, acc) or dfs(i + 1, acc + nums[i])
            cache[(i,acc)] = res

            return res
        
        return dfs(0,0)
            


        