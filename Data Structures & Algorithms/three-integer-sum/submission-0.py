class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            val = nums[i]
            #Ensuring that val is not a duplicate
            if i != 0 and val == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                summation = val + nums[l] + nums[r]
                if summation > 0:
                    r -= 1
                elif summation < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res


        