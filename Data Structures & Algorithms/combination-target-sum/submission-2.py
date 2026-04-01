class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def back(i, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            back(i, total+nums[i])
            path.pop()
            back(i + 1, total)
            return
        
        back(0,0)
        return res

        