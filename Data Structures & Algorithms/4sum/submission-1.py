class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for a,n in enumerate(nums):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                l,r = b + 1, len(nums) - 1

                while l < r:
                    summ = n + nums[b] + nums[l] + nums[r]

                    if summ > target:
                        r -= 1
                    elif summ < target:
                        l += 1
                    else:
                        res.append([n,nums[b],nums[l],nums[r]])

                        l += 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        
        return res