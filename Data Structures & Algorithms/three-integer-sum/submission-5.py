class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            #Window condition
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three = nums[i] + nums[l] + nums[r]

                if three < 0:
                    l += 1
                elif three > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    #keep moving left pointer until left pointer is at 
                    #new value. # Don't forget right pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
        