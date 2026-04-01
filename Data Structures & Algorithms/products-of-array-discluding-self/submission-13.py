class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productFromLeft = {} # Index -> Product of all elements to the left
        curProduct = 1
        for index in range(1, len(nums)):
            
            curProduct *= nums[index - 1]
            productFromLeft[index] = curProduct
            print(productFromLeft)
        curProduct = 1
        productFromRight = {} # index -> product of all elements to the right
        for index in range(len(nums) - 2, -1, -1):
            curProduct *= nums[index + 1]
            productFromRight[index] = curProduct
            print(productFromRight)
        
        output = [0 for i in range(len(nums))]
        output[0] = productFromRight[0]
        output[len(nums) - 1] = productFromLeft[len(nums) - 1]
        for index in range(1, len(nums) - 1):
            output[index] = productFromLeft[index] * productFromRight[index]
        return output

