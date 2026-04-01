class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort(key=lambda x:x[0])

        res = [nums[0]]

        for start,end in nums[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
        
        return res

        