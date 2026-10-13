class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = count = 0

        for num in nums:
            if count == 0:
                maj = num
                count += 1
            elif num != maj:
                count -= 1
            elif num == maj:
                count += 1
        
        return maj


            
