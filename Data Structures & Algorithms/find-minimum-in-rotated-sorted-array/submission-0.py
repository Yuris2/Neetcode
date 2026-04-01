class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) -1

        if nums[l] < nums[r]:
            return res

        while l < r:
            m = (l + r) // 2

            #Think about it in terms of lies beyong
            if nums[m] > nums[r]:
                l = m + 1
            #Right could be the midpoitn
            else:
                r = m
        
        return nums[r]
        



        