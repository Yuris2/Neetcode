class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            val = nums[i]
            #Skipping over iteration if val is equal to previous
            #value
            if i != 0 and val == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                res = nums[l] + nums[r] + val

                if res == 0:
                    ans.append([val, nums[l], nums[r]])

                    l += 1
                    #Keep moving pointer until you find a right
                    #dupe
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif res > 0:
                    r -= 1
                elif res < 0:
                    l += 1
        
        return ans
                    

        